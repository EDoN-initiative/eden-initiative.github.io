---
layout: page
title: News
permalink: /news/
---

{% for post in site.posts %}
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <p><small>{{ post.date | date: "%B %-d, %Y" }}</small></p>
  <p>{{ post.excerpt }}</p>
{% endfor %}