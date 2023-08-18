(function(){
const spanE1 = document.querySelector("main h2 span");
const txtArr = ['Web Publisher','Front-End Developer','Web UI Designer','UX Designer','Back-End Developer'];
let index = 0;
let currentTxt =txtArr[index].split("");
function writeTxt(){
    spanE1.textContent += currentTxt.shift(); //1
    if(currentTxt.length !== 0){/*2*/
        setTimeout(writeTxt, Math.floor(Math.random()*100));
    }
    else{//3
        currentTxt = spanE1.textContent.split("");
        setTimeout(deleteTxt, 3000);
    }
    
}
writeTxt()
function deleteTxt(){
    currentTxt.pop();
    spanE1.textContent = currentTxt.join("");
    if(currentTxt.length !== 0){
        setTimeout(deleteTxt, Math.floor(Math.random()*100));
    }
    else{
        index = (index+1) % txtArr.length;
        currentTxt = txtArr[index].split("");
        writeTxt()
    }
}})();
const headerE1 = document.querySelector("header");
window.addEventListener('scroll',function(){
    this.requestAnimationFrame(scrollcheck);
});
    function scrollcheck(){
    const browerScrollY = window.scrollY ? window.scrollY : window.pageYOffset;
    if(browerScrollY > 0){
        headerE1.classList.add("active");
    }
    else{
        headerE1.classList.remove("active");
    }
}
const animationMove = function(selector){
    const targetE1 = document.querySelector(selector);
    const browerScrollY = window.pageYOffset;
    const targetScrollY = targetE1.getBoundingClientRect().top + browerScrollY;
    window.scrollTo({ top: targetScrollY, behavior: 'smooth'});
};
const scrollMoveE1 = document.querySelectorAll("[data-animation-scroll='true']");
for (let i = 0; i < scrollMoveE1.length; i++) {
    scrollMoveE1[i].addEventListener('click', function (e) {
        const target = this.dataset.target;
        animationMove(target);
    });
}
