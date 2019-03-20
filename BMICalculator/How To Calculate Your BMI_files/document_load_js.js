// When the document loads do everything inside here ...  
$(document).ready(function(){ 
    
    /* prepend menu icon */
	$('#topmenu2').prepend('<div id="menu-icon">Menu</div>');
	/* toggle nav */
	$("#menu-icon").on("click", function(){
		$("#menu_m").slideToggle();
		$(this).toggleClass("active");
	});
	
	/*
	$("select").live("change",function(e) {
		var v = $(this).val();
		var $op = $(this).find("option[value='"+v+"']");
		$(this).parents(".selWrap").find("span").text($op.text());
	});
	*/
    
	//On Click Event for calculator tabs
	$("#mainContent ul.tabs li").click(function() {

		$("#mainContent ul.tabs li").removeClass("active"); //Remove any "active" class
		$(this).addClass("active"); //Add "active" class to selected tab
		$("#mainContent .calculator_form").hide(); //Hide all tab content

		var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
		$(activeTab).show();
		// $(activeTab).fadeIn("fast","linear"); //Fade in the active ID content		
		return false;
	});
		
	//On Click Event for result tabs
	$("#mainContent ul.resulttabs li").click(function() {

		$("#mainContent ul.resulttabs li").removeClass("active"); //Remove any "active" class
		$(this).addClass("active"); //Add "active" class to selected tab
		$("#mainContent .calculator_results").hide(); //Hide all tab content

		var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
		// $(activeTab).fadeIn(); //Fade in the active ID content
		$(activeTab).show();
		return false;
	});
	
	// Changes the focussing of label items on calculators (to show which one is current)
	$(".single-field input").focus(function() {
		$(this).parent().addClass("curFocusDiv")
		$(this).parent().children('label').addClass("curFocus");
	});
	$(".single-field input").blur(function() {
		$(this).parent().removeClass("curFocusDiv");
		$(this).parent().children('label').removeClass("curFocus");
	});
	$(".single-field select").focus(function() {
		$(this).parent().addClass("curFocusDiv")
		$(this).parent().children('label').addClass("curFocus");
	});
	$(".single-field select").blur(function() {
		$(this).parent().removeClass("curFocusDiv");
		$(this).parent().children('label').removeClass("curFocus");
	});
	
	 // This logs an Analytics event when a form is submitted (we have to use the old Analytics code because Ezoic replace the Analytics code in the page with their own old code
	 $('form').submit(function() {
		 _gaq.push(['_trackEvent', 'Profitable Engagement', 'Calculations Made']);
   	 }); 
   	 
   	 // Initiate Analytics event if person has spent more than 3 mins on page
   	 setTimeout("_gaq.push(['_trackEvent', 'Profitable Engagement', 'More than 3 minutes on page'])",180000);
   	 
   	 // This auto-selects the numbers inside a numbers input box, when clicked
   	 $("input[type='number']").click(function () {
   		$(this).select(); this.setSelectionRange(0, this.value.length);
	});
   	 
	// Set the validation message for number boxes.
	// We need to tell them not to use commas.
	var elements = document.getElementsByTagName("INPUT");
    for (var i = 0; i < elements.length; i++) {
    
    	var type = elements[i].getAttribute("type");
        if(type == "number") {

        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Please enter a number into this box. Please do not include commas.");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        }; 	
	    }
    }
	
});

