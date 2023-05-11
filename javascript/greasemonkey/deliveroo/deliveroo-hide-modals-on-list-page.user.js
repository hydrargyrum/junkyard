// ==UserScript==
// @name        deliveroo.fr - don't advertise yourself
// @namespace   Violentmonkey Scripts
// @match       https://deliveroo.fr/fr/restaurants/*
// @grant       none
// @version     1.0
// @author      -
// @description 11/05/2023 11:43:34
// ==/UserScript==

let itv = window.setInterval(function() {
  let button = document.evaluate (
    "//div[@class='ReactModalPortal']//button/span[contains(text(), 'OK')]",
    document.documentElement,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  );
  if (button && button.singleNodeValue) {
    button = button.singleNodeValue;
    button.click();
    window.clearInterval(itv);
  }
}, 1000);
