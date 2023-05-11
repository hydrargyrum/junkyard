// ==UserScript==
// @name        deliveroo.fr - don't suggest me to use the app
// @namespace   Violentmonkey Scripts
// @match       https://deliveroo.fr/fr/orders/*/status
// @grant       none
// @version     1.0
// @author      -
// @description 21/03/2023 11:43:34
// ==/UserScript==

let itv = window.setInterval(function() {
  let button = document.evaluate (
    "//div[@class='ReactModalPortal']//button/span[contains(text(), 'Commander sur le navigateur')]",
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
