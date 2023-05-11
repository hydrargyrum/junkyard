// ==UserScript==
// @name        deliveroo.fr - hide sponsored restaurants
// @namespace   Violentmonkey Scripts
// @match       https://deliveroo.fr/fr/restaurants/*
// @grant       GM_getValue
// @version     1.0
// @author      -
// @description 11/05/2023 11:45:36
// ==/UserScript==

window.setInterval(() => {
  for (el of document.querySelectorAll("a[href*='sp_id=']")) {
      let par = el.parentNode.parentNode.parentNode;
      par.parentNode.removeChild(par);
  }
}, 2000);
