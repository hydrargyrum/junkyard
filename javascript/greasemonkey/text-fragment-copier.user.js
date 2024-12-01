// ==UserScript==
// @name        Text Fragment Copier
// @namespace   Violentmonkey Scripts
// @match       https://*/*
// @version     1.0
// @author      hydrargyrum
// @description Generate text fragment URL pointing to selected text and copy to clipboard (see https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments)
// @grant       GM_registerMenuCommand
// @grant       GM_setClipboard
// ==/UserScript==

GM_registerMenuCommand(
  "Text fragment",
  () => {
    const selectedText = document.getSelection().toString();
    const pageUrl = window.location.href;
    const textToCopy = `${pageUrl}#:~:text=${selectedText}`;

    GM_setClipboard(textToCopy);
  }
);
