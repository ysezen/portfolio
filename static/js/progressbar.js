function progressBar(percent, $element) {
	"use strict";
	let progressBarWidth = percent * $element.width() / 100;
	$element.find('div').animate({ width: percent+'%' }, 500).html("<span>"+percent + "</span>");
}