// document.addEventListener('DOMContentLoaded', function(){
//     document.querySelector("#deal-wheel").querySelectorAll('.prize').forEach(prize => {
//         const rotateValue = getComputedStyle(prize).getPropertyValue('--rotate').trim();
//         if (window.innerWidth <= 576 && (rotateValue === '-90deg' || rotateValue === '-275deg')) {
//             const newRotateValue = rotateValue === '-90deg' ? '-85deg' : '-280deg';
//             prize.style.setProperty('--rotate', newRotateValue);
//         }
//     });
// })