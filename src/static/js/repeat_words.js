$().ready(function() {
    // Process items to be repeated
    $('.item.repeat a').each(function() {
        var $this = $(this);

        var text = $this.text();

        // Remove these comments if spaces are needed
        /*text += ' ';
        $this.html($this.text()+'&nbsp;');*/

        var width = $this.outerWidth();
        var parentWidth = $this.parent('div').outerWidth();

        var numReps = Math.floor(parentWidth / width);

        $this.html(text.repeat(numReps));
    });
});