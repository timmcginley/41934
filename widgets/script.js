
<script>
jQuery.get("https://raw.githubusercontent.com/DTU-Byg/11034/main/A1__Dashboard/readme.md", function(data) {
	var converter = new showdown.Converter(),
    html      = converter.makeHtml(data);
  	$( "#para" ).html( html );
  alert( "Load was performed." );
});
</script>