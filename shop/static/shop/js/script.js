let slider_item = document.getElementsByClassName('slider-item');
let slider = document.querySelectorAll('.slider-item-list');
let Left = document.getElementsByClassName('Left');
let Right = document.getElementsByClassName('Right');
let sld_mrg = 0

function left_change_slide() {
    sld_mrg -=500
    switch (sld_mrg) {
        case slider_item.length * - 500 :
            sld_mrg = 0;
          break;
        case 500:
          sld_mrg = -slider_item.length * 500 + 500;
          break;
      }
      console.log(sld_mrg)
      slider[0].style = `margin-left: ${sld_mrg}px`;
}

function right_change_slide() {
    sld_mrg +=500
    switch (sld_mrg) {
        case slider_item.length * -500 :
            sld_mrg = 0;
          break;
        case 500:
          sld_mrg = slider_item.length * -500 + 500;
          break;
      }
      console.log(sld_mrg)
      slider[0].style = `margin-left: ${sld_mrg}px`;
}

Left[0].addEventListener("click", left_change_slide);
Right[0].addEventListener("click", right_change_slide);
