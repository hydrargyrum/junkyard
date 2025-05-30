// ==UserScript==
// @name        instagram.com - download post images in a JSON archive
// @namespace   Violentmonkey Scripts
// @match       https://www.instagram.com/p/*
// @match       https://www.instagram.com/*/p/*
// @version     1.0
// @author      -
// @description 14/04/2025 21:58:07
// @grant       GM_registerMenuCommand
// ==/UserScript==

const imageCandidateRegex = /\s*([^,]\S*[^,](?:\s+[^,]+)?)\s*(?:,|$)/;

// stolen from https://github.com/sindresorhus/srcset under MIT license
function parseSrcset(string) {
	return string
		.replace(/\r?\n/, '')
		.replace(/,\s+/, ', ')
		.split(imageCandidateRegex)
		.filter((part, index) => index % 2 === 1)
		.map(part => {
			const [url, ...descriptors] = part.trim().split(/\s+/);

			const result = {url};

			for (const descriptor of descriptors) {
				const postfix = descriptor[descriptor.length - 1];
				const value = Number.parseFloat(descriptor.slice(0, -1));

				switch (postfix) {
					case 'w': {
						result.width = value;
						break;
					}

					case 'h': {
						result.height = value;
						break;
					}

					case 'x': {
						result.density = value;
						break;
					}

					// No default
				}
			}

			return result;
		});
}


function addLink() {
  let page_id = document.location.pathname.match(/\/p\/([\w-]+)/)[1];

  let n = 0;
  let promises = [];
  for (let img of document.querySelectorAll("div>div>div>img")) {
    n++;
    let n_str = `${n}`.padStart(2, "0");
    let filename = `instagram-${page_id}-${n_str}.jpg`;
    let besturl;
    if (img.srcset) {
      let srcset = parseSrcset(img.srcset);
      srcset.sort((a, b) => a.width - b.width);
      srcset.reverse();
      besturl = srcset[0].url;
    } else {
      besturl = img.src;
    }

    promises.push(fetch(besturl).then(async(response) => {
      let blob = await response.blob();
      let data = await blob.bytes();
      return {
        "filename": filename,
        "data": data.toBase64(),
      }
    }));
  }

  Promise.all(promises).then((values) => {
    let container = document.querySelector("main");
    let link = document.createElement("a");

    link.innerText = "Download JSON archive";
    link.style.margin = "1em";
    link.setAttribute("download", `instagram-${page_id}.archive.json`);
    link.setAttribute("href", URL.createObjectURL(new Blob([JSON.stringify(values)])));

    container.insertBefore(link, container.firstChild);
  });
}

function goAllNext() {
  let itv = window.setInterval(() => {
    let button = document.querySelector('button[aria-label="Suivant"]');
    if (button) {
      button.click();
    } else {
      window.clearInterval(itv);
      addLink();
    }
  }, 100);
}

GM_registerMenuCommand(
  "build image links",
  () => {
    goAllNext();
  }
);
