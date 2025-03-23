const wheel = document.querySelector("#deal-wheel");

const context_nanny = wheel.querySelector('#spinner-nanny')
const spinnerNanny = context_nanny.querySelector(".spinner");
const trigger_nanny = context_nanny.querySelector(".btn-spin");
const ticker_nanny = context_nanny.querySelector(".ticker");
const prizeNodesNanny = context_nanny.querySelectorAll(".prize");

const context_parent = wheel.querySelector('#spinner-parent')
const spinnerParent = context_parent.querySelector(".spinner");
const trigger_parent = context_parent.querySelector(".btn-spin");
const ticker_parent = context_parent.querySelector(".ticker");
const prizeNodesParent = context_parent.querySelectorAll(".prize");

let tickerAnim;
let rotation = 0;
let currentSlice = 0;

const spinClass = "is-spinning";
const selectedClass = "selected";

let spinnerStyles;

const spinertia = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

const runTickerAnimation = () => {
    const values = spinnerStyles.transform.split("(")[1].split(")")[0].split(",");
    const a = values[0];
    const b = values[1];  
    let rad = Math.atan2(b, a);
    if (rad < 0) rad += (2 * Math.PI);
    tickerAnim = requestAnimationFrame(runTickerAnimation);
};

const selectPrize = (prizeNodes, prizeSlice, numSlices) => {
    const selected = Math.floor(rotation / prizeSlice) % numSlices;
    prizeNodes[selected].classList.add(selectedClass);
};

const setPrize = (is_nanny) => {
    if(is_nanny) {
        const context = wheel.querySelector('#spinner-nanny')
        const btn = context.querySelector('.btn-spin')
        const promoBlock = context.querySelector(".win");
        promoBlock.removeAttribute('hidden')
        promoBlock.addEventListener("click", () => {
        const textToCopy = "NANNY";
        navigator.clipboard.writeText(textToCopy)
            .then(() => {
                alert("Промокод скопирован: " + textToCopy);
            })
            .catch((err) => {
                console.error("Не удалось скопировать текст: ", err);
            });
        });
        btn.remove()
    }
    else {
        const context = wheel.querySelector('#spinner-parent')
        const promoBlock = context.querySelector(".win");
        const btn = context.querySelector('.btn-spin')
        promoBlock.removeAttribute('hidden')
        promoBlock.addEventListener("click", () => {
        const textToCopy = "PARENT";
        navigator.clipboard.writeText(textToCopy)
            .then(() => {
                alert("Промокод скопирован: " + textToCopy);
            })
            .catch((err) => {
                console.error("Не удалось скопировать текст: ", err);
            });
        });
        btn.remove()
    }
    
    
}

const stopAtPrize = (spinner, prizeSlice, prizeIndex) => {
    const targetRotation = prizeIndex * prizeSlice + (360 * Math.round(Math.random() * 6)) + Math.round(Math.random() * 10); // 5 полных оборотов для эффекта
    rotation = targetRotation;
    spinner.style.setProperty("--rotate", rotation);
};


trigger_nanny.addEventListener("click", () => {
    trigger_nanny.disabled = true;
    spinnerStyles = window.getComputedStyle(spinnerNanny);
    wheel.classList.add(spinClass);
    ticker_nanny.style.animation = "none";
    const desiredPrizeIndex = 3;
    const numSlices = prizeNodesNanny.length;
    const prizeSlice = 360 / numSlices;
    stopAtPrize(spinnerNanny, prizeSlice, desiredPrizeIndex);
    runTickerAnimation();
});


trigger_parent.addEventListener("click", () => {
    trigger_parent.disabled = true;
    spinnerStyles = window.getComputedStyle(spinnerParent);
    wheel.classList.add(spinClass);
    ticker_parent.style.animation = "none";
    const desiredPrizeIndex = 2;
    const numSlices = prizeNodesParent.length;
    const prizeSlice = 360 / numSlices;
    stopAtPrize(spinnerParent, prizeSlice, desiredPrizeIndex);
    runTickerAnimation();
});


spinnerNanny.addEventListener("transitionend", () => {
    cancelAnimationFrame(tickerAnim);
    rotation %= 360;
    const numSlices = prizeNodesNanny.length;
    const prizeSlice = 360 / numSlices;
    selectPrize(prizeNodesNanny, prizeSlice, numSlices);
    wheel.classList.remove(spinClass);
    spinnerNanny.style.setProperty("--rotate", rotation);
    setPrize(true)
});


spinnerParent.addEventListener("transitionend", () => {
    cancelAnimationFrame(tickerAnim);
    rotation %= 360;
    const numSlices = prizeNodesParent.length;
    const prizeSlice = 360 / numSlices;
    selectPrize(prizeNodesParent, prizeSlice, numSlices);
    wheel.classList.remove(spinClass);
    spinnerParent.style.setProperty("--rotate", rotation);
    setPrize(false)
});