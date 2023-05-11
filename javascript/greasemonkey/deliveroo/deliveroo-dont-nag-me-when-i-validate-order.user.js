// ==UserScript==
// @name        deliveroo.fr - don't nag me with modals when i validate order
// @namespace   Violentmonkey Scripts
// @match       https://deliveroo.fr/fr/menu/*
// @grant       none
// @version     1.0
// @author      -
// @description 23/10/2022 12:13:01
// ==/UserScript==

window.setInterval(function() {
  // no, my order is fine, i don't want to add more dishes
  let button = document.evaluate (
    "//div[@class='ReactModalPortal']//button/span[contains(text(), 'Finaliser la commande')]",
    document.documentElement,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  );
  if (button && button.singleNodeValue) {
    button = button.singleNodeValue;
    button.click();
    // don't kill timer because there might be several buttons in a row, what a pain…
  }
}, 1000);

let itv = window.setInterval(function() {
  // no, i won't tip the delivery before i receive the delivery!
  let button = document.evaluate (
    "//div[@class='ReactModalPortal']//a/span[contains(text(), 'Plus tard')]",
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

