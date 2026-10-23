/* Shared chart helpers. Plain JS, no dependencies. Exposes window.VZ. */
(function(){
var NS="http://www.w3.org/2000/svg";
var VZ={};
/* create an SVG element: VZ.el("rect",{x:0,...},parent) */
VZ.el=function(tag,attrs,parent){var e=document.createElementNS(NS,tag);for(var k in attrs||{})e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e};
VZ.svg=function(host,w,h,label){var s=VZ.el("svg",{viewBox:"0 0 "+w+" "+h,role:"img","aria-label":label||""});host.appendChild(s);return s};
/* linear scale */
VZ.lin=function(d0,d1,r0,r1){return function(v){return r0+(v-d0)/(d1-d0)*(r1-r0)}};
/* read a CSS custom property, e.g. VZ.c("--s1") */
VZ.c=function(name){return getComputedStyle(document.documentElement).getPropertyValue(name).trim()};
/* the series colour as a CSS var reference, slot 1..8 */
VZ.s=function(i){return "var(--s"+i+")"};
/* bar with 4px rounded data end and square baseline. horizontal if dir="h" */
VZ.bar=function(parent,x,y,w,h,fill,dir){var r=Math.min(4,dir==="h"?h/2:w/2,dir==="h"?w:h);var d;
 if(w<=0||h<=0)d="";
 else if(dir==="h")d="M"+x+","+y+"h"+(w-r)+"a"+r+","+r+" 0 0 1 "+r+","+r+"v"+(h-2*r)+"a"+r+","+r+" 0 0 1 -"+r+","+r+"h-"+(w-r)+"z";
 else d="M"+x+","+(y+h)+"v-"+(h-r)+"a"+r+","+r+" 0 0 1 "+r+",-"+r+"h"+(w-2*r)+"a"+r+","+r+" 0 0 1 "+r+","+r+"v"+(h-r)+"z";
 return VZ.el("path",{d:d,fill:fill},parent)};
/* tooltip: VZ.tip(el, function(){return "<b>Title</b>text"}) ; works with mouse, touch and keyboard focus */
var tip;function T(){if(!tip){tip=document.createElement("div");tip.className="vz-tip";tip.setAttribute("role","tooltip");document.body.appendChild(tip)}return tip}
function place(x,y){var t=T(),w=t.offsetWidth,h=t.offsetHeight,X=x+14,Y=y+14;if(X+w>innerWidth-8)X=x-w-14;if(Y+h>innerHeight-8)Y=y-h-14;t.style.left=Math.max(8,X)+"px";t.style.top=Math.max(8,Y)+"px"}
VZ.tip=function(el,fn){
 el.addEventListener("pointerenter",function(e){var t=T();t.innerHTML=fn();t.classList.add("on");place(e.clientX,e.clientY)});
 el.addEventListener("pointermove",function(e){place(e.clientX,e.clientY)});
 el.addEventListener("pointerleave",function(){T().classList.remove("on")});
 if(!el.hasAttribute("tabindex"))el.setAttribute("tabindex","0");
 el.addEventListener("focus",function(){var t=T(),r=el.getBoundingClientRect();t.innerHTML=fn();t.classList.add("on");place(r.left+r.width/2,r.top+r.height/2)});
 el.addEventListener("blur",function(){T().classList.remove("on")});
};
VZ.hideTip=function(){if(tip)tip.classList.remove("on")};
/* tabs: container with [role=tablist] buttons[role=tab][aria-controls] */
VZ.tabs=function(list,onChange){var tabs=[].slice.call(list.querySelectorAll("[role=tab]"));
 function sel(t){tabs.forEach(function(x){var on=x===t;x.setAttribute("aria-selected",on);x.tabIndex=on?0:-1;var p=document.getElementById(x.getAttribute("aria-controls"));if(p)p.hidden=!on});if(onChange)onChange(t)}
 tabs.forEach(function(t,i){t.addEventListener("click",function(){sel(t)});t.addEventListener("keydown",function(e){var k=e.key==="ArrowRight"?1:e.key==="ArrowLeft"?-1:0;if(k){var n=tabs[(i+k+tabs.length)%tabs.length];n.focus();sel(n)}})});
 sel(tabs.filter(function(t){return t.getAttribute("aria-selected")==="true"})[0]||tabs[0]);};
/* count up numbers: <b class="count" data-to="22" data-suffix="%"> */
function count(el){var to=parseFloat(el.dataset.to),dec=(el.dataset.to.split(".")[1]||"").length,pre=el.dataset.prefix||"",suf=el.dataset.suffix||"",t0=null;
 if(matchMedia("(prefers-reduced-motion: reduce)").matches){el.textContent=pre+to.toLocaleString("en-GB",{minimumFractionDigits:dec,maximumFractionDigits:dec})+suf;return}
 function f(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/1100),v=to*(1-Math.pow(1-p,3));el.textContent=pre+v.toLocaleString("en-GB",{minimumFractionDigits:dec,maximumFractionDigits:dec})+suf;if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
/* reveal on scroll: add class "rv" to anything; ".count" inside counts up */
VZ.reveal=function(){var els=[].slice.call(document.querySelectorAll(".rv,.count"));
 if(!("IntersectionObserver" in window)){els.forEach(function(e){e.classList.add("in");if(e.classList.contains("count"))count(e)});return}
 var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");if(en.target.classList.contains("count"))count(en.target);io.unobserve(en.target)}})},{threshold:.15});
 els.forEach(function(e){io.observe(e)})};
/* redraw on theme toggle: VZ.onTheme(fn) */
VZ.onTheme=function(fn){new MutationObserver(fn).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});matchMedia("(prefers-color-scheme: dark)").addEventListener("change",fn)};
window.VZ=VZ;
document.addEventListener("DOMContentLoaded",VZ.reveal);
})();
