var my_index = 0;
    carousel();

    function carousel() {
        var i;
        var x = document.getElementsByClassName("mySlides");

        for (i=0; i < x.length; i++) {
            x[i].style.display = "none";
        }

        my_index++;

        if (my_index > x.length) {
            my_index = 1;
        }

        x[my_index-1].style.display = "block";
        setTimeout(carousel, 2000); //change image every 2 seconds
    }