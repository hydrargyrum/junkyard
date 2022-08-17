// ==UserScript==
// @name        * - Round prices
// @namespace   Violentmonkey Scripts
// @match       https://*/*
// @grant       none
// @version     1.0
// @author      hydrargyrum
// @description 29/06/2022 22:07:09
// ==/UserScript==

function littleRound(nb) {
  let factors = [.01, .1, 1, 10];
  for (let factor of factors) {
    let rounded = Math.ceil(nb * factor) / factor;
    // console.log(nb, factor, rounded, rounded / nb);
    if (rounded / nb <= 1.1) {
      return rounded;
    }
  }

  return nb;
}

function parseFloatLocales(s) {
  // accepts "1,234.56" or "1.234,56" or "1 234,56"
  s = s.replaceAll(" ", "");
  s = s.replaceAll(",", ".");
  s = s.replaceAll(/\.(\d{3})/g, "\1");
  return parseFloat(s);
}

function replaceInTextNode(node) {
  node.data = node.data.replaceAll(
    /\b(\d{1,3}([., ]\d{3})*([.,]\d{2})?)\b/g,
    (match, nb_s) => {
      let nb = parseFloatLocales(nb_s);
      let rounded = littleRound(nb);
      if (nb != rounded) {
        return "~" + rounded.toFixed(2);
      }
      return nb_s;
    }
  );
}

// unfortunately will not work with "1$99"
// or if decimals are in separate tag

function recurse(elem) {
  for (let sub of elem.childNodes) {
    switch (sub.nodeType) {
      case Node.ELEMENT_NODE:
        if (sub.tagName != "style" && sub.tagName != "script") {
          recurse(sub);
        }
        break;
      case Node.TEXT_NODE:
        replaceInTextNode(sub);
        break;
      default:
        break;
    }
  }
}

window.addEventListener("load", (event) => {
  recurse(document.body);
});
