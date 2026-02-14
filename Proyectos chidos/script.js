const siBtn = document.getElementById("si");
const noBtn = document.getElementById("no");

siBtn.addEventListener("click", function(){
  alert("Sabía que dirías que sí 😍💘 Feliz 14 de febrero");
});

noBtn.addEventListener("mouseover", function(){
  noBtn.style.top = Math.random()*200 + "px";
  noBtn.style.left = Math.random()*200 + "px";
});