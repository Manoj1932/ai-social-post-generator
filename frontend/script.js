function scrollToGenerator(){

document.getElementById("generator")
.scrollIntoView({behavior:"smooth"})

}



function useTemplate(topic,platform){

document.getElementById("topic").value = topic
document.getElementById("platform").value = platform

scrollToGenerator()

}



async function generate(){

const platform = document.getElementById("platform").value
const topic = document.getElementById("topic").value
const tone = document.getElementById("tone").value

document.getElementById("loading").style.display="block"
document.getElementById("result").innerText=""

const response = await fetch("https://ai-social-post-generator-n2ie.onrender.com/generate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
platform:platform,
topic:topic,
tone:tone
})

})

const data = await response.json()

document.getElementById("loading").style.display="none"

document.getElementById("result").innerText=data.content

}



function copyText(){

const text=document.getElementById("result").innerText

navigator.clipboard.writeText(text)

const btn=document.querySelector(".copy-btn")

btn.innerText="✅ Copied!"

setTimeout(()=>{
btn.innerText="📋 Copy"
},2000)

}

// FAQ toggle

const faqQuestions = document.querySelectorAll(".faq-question");

faqQuestions.forEach(question => {
  question.addEventListener("click", () => {

    const answer = question.nextElementSibling;

    if(answer.style.maxHeight){
      answer.style.maxHeight = null;
    } else {
      answer.style.maxHeight = answer.scrollHeight + "px";
    }

  });
});

function copyExample(btn){

const text = btn.parentElement.querySelector("p").innerText
navigator.clipboard.writeText(text)

btn.innerText = "Copied!"

setTimeout(()=>{
btn.innerText = "Copy"
},2000)

}