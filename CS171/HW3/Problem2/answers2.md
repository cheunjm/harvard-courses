<p>Problem 2 Answers:</p>
 
<ol>
<li>
The data types are integers (for the table head, it is strings). It is different from the datasets I have used before in that there are some missing data, and there are data from many categories. 
</li>
<li>
To get the second row in the Wikipedia table:
            var content = root.find("#content"); // find all the nodes that have ID "content"
            var h2s = content.find(".mw-headline"); // search in all "content" nodes for nodes of class ".mw-headline"
            var wikitable = content.find(".wikitable");
            var rows = wikitable.find("tbody tr");
            $.each(rows,function(index, value) {
              if(index == 1)// second row
              {
                return rows(index);
              } 
            })
to get all table rows that are not in the Wikipedia table,
           var content = root.find("#content"); // find all the nodes that have ID "content"
            var h2s = content.find(".mw-headline"); // search in all "content" nodes for nodes of class ".mw-headline"
            var wikitable = content.find(".wikitable");
            var rows = wikitable.find("tbody tr");
            $.each(rows,function(index, value) {
              if(index == 0)// for the header case
              {
                //Do nothing
              } 
              else {
                return rows[index];
              }

            })
</li>
</ol>
