
## **Overview**

Parsing is an essential process for browser's rendering engine which basically translates the HTML document to a structure which a the browser's code can use.
The process is based on a syntax rules which the HTML document obeys which is specified in HTML5 Specification
 > Explained in detail [HTML5 Specification](https://html.spec.whatwg.org/multipage/parsing.html "HTML5 Specification")

The result of parsing is usually a tree of nodes i.e the structure of the document.

#### **Overall Flow**
----

**DOM:**
1. The input to the HTML parsing consists a stream of unicode characters which is actually a sequence of bytes coming over the network or your local file system.
2. Input is than passed through tokenization stage followed by a tree construction stage
    * **Tokenization:**
        - It is the process of breaking down a sequence of character into `HTML tokens` like `start tags, end tags, attribute names, attribute values`.
        - The tokenizer recognizes the token, gives it to the tree constructor, and consumes the next character for recognizing the next token, and so on until the end of the input.
        >Without the tokenization process, the browser would just render characters in the input stream as text displaying the html file as it is without rendering it into a webpage.

    * **Tree construction:**
        - During this stage the DOM tree with the Document in its root is created
        - The Nodes emitted by the tokenizer are processed by the tree constructor and are linked to the tree structure which is the DOM.

    > A stack of open elements is also maintained which is used to correct nesting mismatches and unclosed tags.

        The Output:
        + For HTML it is the DOM Tree
        + For CSS it is the CSSOM Tree.

**The whole process can be summarised as:**

        "Bytes ==> Characters ==> Tokens ==> Nodes ==> DOM"

Example:

```
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link href="style.css" rel="stylesheet">
    <title>Critical Path</title>
  </head>
  <body>
    <p>Hello <span>web performance</span> students!</p>
    <div><img src="awesome-photo.jpg"></div>
  </body>
</html>
```

The above example would undergo following process.

![Browser Processing  ](https://kbassets.sgp1.digitaloceanspaces.com/1551774311886-full-process.png)

**CSSOM**

The DOM tree captures the properties and relationships of the document markup, but it doesn't tell us how the element will look when rendered. That’s the responsibility of the CSSOM.

Given the above code snippet, as soon as the browser encounters the link tag referring to an external `.CSS ` file it requests the following file.

The response would look like:

```
body { font-size: 16px }
p { font-weight: bold }
span { color: red }
p span { display: none }
img { float: right }
```

Now we repeat the HTML process, but for CSS:

      "Bytes ==> Characters ==> Tokens ==> Nodes ==> CSSOM"

The CSS Object Model:

![CSSOM](https://kbassets.sgp1.digitaloceanspaces.com/1551783143377-cssom-tree.png)

Now we have two independent tress where the **DOM** contains infromation about HTML element's relationships, While the **CSSOM** contains information on how these elements are styled.

The Browser Combines these two trees to form a **Render Tree**.

The **Render Tree** goes through the layout and Painting process.

During Layout Process every node is given exact coordinates to where to appear on the browser screen and the painting process involves displaying the rendered tree using the UI backend.

The EOF file is indicated by document.close() or if there is a lack of any further characters in the input stream
