const wheel = document.querySelector("#deal-wheel");
let spinner = wheel.querySelector(".spinner");
const triggers = wheel.querySelectorAll(".btn-spin");
const ticker = wheel.querySelector(".ticker");
const prizeNodes = wheel.querySelectorAll(".prize");

const context_nanny = wheel.querySelector('#spinner-nanny')
const spinner_nanny = context_nanny.querySelector(".spinner");
const trigger_nanny = context_nanny.querySelectorAll(".btn-spin");
const ticker_nanny = context_nanny.querySelector(".ticker");
const prizeNodes_nanny = context_nanny.querySelectorAll(".prize");

const context_parent = wheel.querySelector('#spinner-parent')
const spinner_parent = context_nanny.querySelector(".spinner");
const trigger_parent = context_nanny.querySelectorAll(".btn-spin");
const ticker_parent = context_nanny.querySelector(".ticker");
const prizeNodes_parent = context_nanny.querySelectorAll(".prize");

let tickerAnim;
let rotation = 0;
let currentSlice = 0;

const spinClass = "is-spinning";
const selectedClass = "selected";

let spinnerStyles;
const numSlices = prizeNodes.length;
const prizeSlice = 360 / numSlices;

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

const selectPrize = () => {
    const selected = Math.floor(rotation / prizeSlice) % numSlices;
    prizeNodes[selected].classList.add(selectedClass);
};

const setPrize = () => {
    if(wheel.querySelector('#spinner-nanny-tab').getAttribute('aria-selected') === 'true') {
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

const stopAtPrize = (prizeIndex) => {
    const targetRotation = prizeIndex * prizeSlice + (360 * Math.round(Math.random() * 6)); // 5 полных оборотов для эффекта
    rotation = targetRotation;
    spinner.style.setProperty("--rotate", rotation);
};


trigger_nanny.addEventListener("click", () => {
    trigger_nanny.disabled = true;
    spinnerStyles = window.getComputedStyle(spinner_nanny);
    wheel.classList.add(spinClass);
    ticker.style.animation = "none";
    const desiredPrizeIndex = 4;
    stopAtPrize(desiredPrizeIndex);
    runTickerAnimation();
});


trigger_parent.addEventListener("click", () => {
    trigger_nanny.disabled = true;
    spinnerStyles = window.getComputedStyle(spinner_parent);
    wheel.classList.add(spinClass);
    ticker.style.animation = "none";
    const desiredPrizeIndex = 4;
    stopAtPrize(desiredPrizeIndex);
    runTickerAnimation();
});


triggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
        if(wheel.querySelector('#spinner-nanny-tab').getAttribute('aria-selected') === 'true') {
            spinner = wheel.querySelector('#spinner-nanny').querySelector('.spinner');
            spinnerStyles = window.getComputedStyle(spinner);
        }
        else {
            spinner = wheel.querySelector('#spinner-parent').querySelector('.spinner');
            spinnerStyles = window.getComputedStyle(spinner);
        }
        trigger.disabled = true;
        wheel.classList.add(spinClass);
        ticker.style.animation = "none";
        const desiredPrizeIndex = 4;
        stopAtPrize(desiredPrizeIndex);
        runTickerAnimation();
    });
})


spinner.addEventListener("transitionend", () => {
    cancelAnimationFrame(tickerAnim);
    rotation %= 360;
    selectPrize();
    wheel.classList.remove(spinClass);
    spinner.style.setProperty("--rotate", rotation);
    setPrize()
});