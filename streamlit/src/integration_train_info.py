integration_info = """
Provenance is a platform for brands and retailers to build trust in their products through supply chain communication and storytelling.
Provenance offers two types of embeds: bundles and experiences.
Bundles are collections of Proof Points (or schemes) scoped by brand or product.
Experiences are customizable pages made of components (Map, Journey, Story, Proof Points) that tell the story of a product.
The Provenance SDK enables the integration of embeds and a Trust Badge into customer websites.
Embeds require the provenance-sdk library and a custom element (<provenance-experience> or <provenance-bundle>) with an embed URL.
The Trust Badge is a visual indicator that a product has Provenance content and can be added to web pages.
The Trust Badge is typically placed above the fold and clicking on it scrolls the page to the Proof Points.
The Trust Badge automatically appears or disappears based on the presence of Provenance content on the page.
To add the Trust Badge, use the <provenance-trust-badge access-token=YOUR_TOKEN_HERE> custom element.
The <provenance-bundle> element should have the id=provenance-trust-badge attribute.
An access token is required for the Trust Badge and can be obtained from a support representative.
To load the Provenance SDK library and embeds, add a script tag with defer="" and src="https://unpkg.com/@provenance/provenance-sdk@1/dist/provenance-sdk.js" to the closing </body> tag of your site.
here is an example of how standard integration code would look on a site:
<body>
// top of your site ending around your product title
<provenance-trust-badge access-token="eea408e8-1b08-4815-8df5-ede8789323ab"></provenance-trust-badge>
# some other content in your site ending around the add to cart button
    <provenance-bundle id="provenance-trust-badge"               url="https://www.provenance.org/bundles/Q3aqVROa/embed"     ></provenance-bundle>
// the rest of the content of your site
<script type="application/ld+json">
    {
      "@context": "http://schema.org/",
      "@type": "Product",
      "sku": "1077"
    }
  </script>

<script defer=""
src="https://unpkg.com/@provenance/provenance-sdk@1/dist/provenance-sdk.js"></script>
</body>


note: if you output code in your answer, please put this on a different line to regular text.
"""