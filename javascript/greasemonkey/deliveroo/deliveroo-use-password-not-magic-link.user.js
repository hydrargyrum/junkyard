// ==UserScript==
// @name        deliveroo.fr - choose password method at login (not magic link)
// @namespace   Violentmonkey Scripts
// @match       https://deliveroo.fr/fr/login
// @grant       none
// @version     1.0
// @author      -
// @description 18/10/2022 11:47:32
// ==/UserScript==

let itv2 = window.setInterval(function() {
  let button = document.querySelector("#continue-with-email");
  if (button) {
    window.clearInterval(itv2);
    button.click();
  }
}, 500);

let itv1 = window.setInterval(function() {
  let passwordbutton = document.querySelector("#type-password-btn");
  if (passwordbutton) {
    window.clearInterval(itv1);
    passwordbutton.click();
  }
}, 500);
