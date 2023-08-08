window.onload = () =>{
    const errorMsg = document.querySelector("#error-msg");
    if(errorMsg){
        const loginForm = document.querySelector("#login-form");
        const amountElements = loginForm.children.length;
        for(let i = 0; i < amountElements; i++){
            let element = loginForm.children[i];
            if(element.tagName == "INPUT" && element.type != "hidden"){
                element.classList.add("error-values");
            }
        }
    }
}