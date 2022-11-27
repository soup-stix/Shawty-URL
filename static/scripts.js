

    //document.getElementById("submit").addEventListener("click", submitAction);
    document.getElementById("copy").addEventListener("click", copyAction);
    

    /*function submitAction() {
        var copyText = document.getElementById("myInput");
        console.log(copyText.value);
        var element = document.getElementById('tooltip');
        element.style.visibility = 'visible';
    }*/

    function copyAction() {
        var tooltip = document.getElementById("myTooltip");
        tooltip.innerHTML = "Copied!";
        console.log(copyText);
    }