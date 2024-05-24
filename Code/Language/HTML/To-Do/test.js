let message = `
In October 1994, Tim Berners-Lee founded an organization—the World Wide Web Consortium (W3C)—devoted to developing nonproprietary, interoperable technologies for the World Wide Web. One of the W3C’s primary goals is to make the web universally accessible—regardless of disability, language or culture. The W3C home page (www.w3.org) provides extensive resources on Internet and web technologies.
The W3C is also a standards organization. Web technologies standardized by the W3C are called Recommendations. Current and forthcoming W3C Recommendations include the HyperText Markup Language 5 (HTML5), Cascading Style Sheets 3 (CSS3) and the Extensible Markup Language (XML). A recommendation is not an actual software product but a document that specifies a technology’s role, syntax rules and so forth.
1.10 Web 2.0: Going Social
In 2003 there was a noticeable shift in how people and businesses were using the web and developing web-based applications. The term Web 2.0 was coined by Dale Dougherty of O’Reilly Media4 in 2003 to describe this trend. Generally, Web 2.0 companies use the web as a platform to create collaborative, community-based sites (e.g., social networking sites, blogs, wikis).
`;
let sentances = message.split(/[.!?]/);
console.log(sentances);
document.getElementById("t1").innerHTML = sentances + "/n";

function myFunction() { //01 create function
    const list = document.getElementById("myDIV").classList;
    list.add("myStyle");
  }
  