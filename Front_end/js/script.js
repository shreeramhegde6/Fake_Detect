<script>
  function check_link()
  {
  var url = document.getElementById("search").value
  var domain = url = url.replace(/^(?:https?:\/\/)?(?:www\.)?/i, "").split('/')[0];
  console.log(httpGet(domain));
  }

  function httpGet(theUrl)
{
    //theUrl = "http://www.fakenewsai.com/detect?url=http%3A%2F%2F" + theUrl;
    //var data1 = {"URL":theUrl};
    var url = "/dorequest?url="+theUrl;
$.ajax({
	async: false,
	type: 'GET',
	url : url,
	success: function(data) {
		console.log(data);
		var res = data["data"];
		if (res["error"] == true)
		{ swal ( "Oops" ,  "Looks like we don't have any data on the website!" ,  "error" );
	}
	else
	{
	if(res["fake"] == false )
	 swal("Safe", "The news is not fake!", "success");
	}
	if(res["fake"] == true )
	{
	swal ( "Fake" ,  "Looks like the website serves fake content!" ,  "error" );
	}
	}
});
}


</script>