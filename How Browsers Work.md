## **The Browser's High Level Structure**

---------------------
![Browser Structure](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/layers.png)

>* __The User Interface:__ Includes all the UI elements like Address bar,Back and forword buttons, Bookmaring window etc.  
* __Browser Engine:__ Queries the rendering engine based on the input given to UI. Acts as a mediator between UI and Rendering Engine.
* __The Rendering Engine:__  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Displays requested contentparses  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Parses HTML/XML tags,images. Using the styles and css attributes it builds a render tree and then creates a render layout.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* The rendering engine can also display other media like PDF's  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* render layout is displayed on the screen.  

>                    "Each Tab is a different process with it's own Rendering Engine."
* __Networking:__ responsible for netwoking calls like HTTP requests and other protocols based on platforms
* __UI Backend:__ does the job of drawing widgets like checkboxes, textboxes etc based on css attributes.
* __JavaScript Interpreter:__   interpretes the javascript code
* __Data Storage:__ cookies,localstorage,sessions etc.

## **The rendering engine**
----

>1. The rendering engine will parse the HTML and convert the elements into ` DOM tree `.  
2. Then, the engine will parse the style data including the external CSS files and create a ` render tree ` which consits of HTML document with the added styles.  
3. The ` render tree ` goes through a ` layout ` process where the nodes are given exact coordinates where it should appear on the screen.
4. `Painting` is the next process where the `render tree` is traversed and each node is painted in the screen using the `UI backend layer`.   
5. Webkit uses the term `Attachment` for the process of connecting the DOM nodes and visual information like styling and padding etc. to create a `render tree` while Gecko uses an extra layer between HTML and DOM called as content sink.
6.  Gecko Calls the `render tree` as `frame tree` and each element in the frame is a `frame`.

* Internet Explorer: Trident
* Firefox & other Mozilla browsers: Gecko
* Chrome & Opera 15+: Blink
* Chrome (iPhone) & Safari: Webkit


##### **Flow Diagram:**
----

![webkit Flow](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/webkitflow.png)
