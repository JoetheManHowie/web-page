const header = document.querySelector('header');
const nav = document.createElement('nav');
const ul = document.createElement('ul');

const links = [    {text: 'Home', href: 'home.html'},
{text: 'About', href: 'about.html'},
{text: 'Blog', href: 'blog.html'},
{text: 'Contact', href: 'contact.html'},];

for (let i = 0; i < links.length; i++) {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.textContent = links[i].text;
    a.setAttribute('href', links[i].href);
    li.appendChild(a);
    ul.appendChild(li);
}

nav.appendChild(ul);
header.appendChild(nav);
