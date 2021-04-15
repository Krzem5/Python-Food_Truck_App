document.addEventListener("DOMContentLoaded",()=>{
	let ne=document.querySelector(".nav");
	let me=document.querySelector(".menu");
	window.onresize=()=>{
		me.style.minHeight=`${document.body.clientHeight-ne.getBoundingClientRect().bottom}px`;
	};
	setInterval(window.onresize,100);
},false);
