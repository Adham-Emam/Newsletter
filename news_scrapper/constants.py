URLS = [
    "https://alhkaia.com/",
    "https://almontag.com/",
    "https://altibbi.com/",
    "https://app.lesite24.com/",
    "https://ar.ra2ya.com/",
    "https://arab.sahafahh.net/",
    "https://arabic.sport360.com/",
    "https://aramland.com/",
    "https://clubtc.net",
    "https://gate.ahram.org.eg/",
    "https://highwia.com/",
    "https://jo.motory.com/ar/",
    "https://jordanrec.com/",
    "https://m.sa24.co/",
    "https://mawdoo3.com/",
    "https://mesrena.com/",
    "https://mhtwyat.com/",
    "https://misr-post.com/",
    "https://mj.bald-news.com/",
    "https://mobizil.com/",
    "https://molhamon.com",
    "https://mostakpel.com/",
    "https://mz-mz.net/",
    "https://news.faharas.net/",
    "https://newso.elsob7.com/",
    "https://royanews.tv/",
    "https://sa.tqwem.com/",
    "https://shbabbek.com/",
    "https://shootz.yalla-shoot-tv.live/home18/",
    "https://takeitright2022.com",
    "https://trend.nl7za.com/",
    "https://trends.khbrny.com/",
    "https://wikieurope.net/",
    "https://ww.kuwaitpress.net",
    "https://www.arabiaweather.com/",
    "https://www.elbalad.news/",
    "https://www.khaberni.com/",
    "https://www.kooora.com/",
    "https://www.masrawy.com/",
    "https://www.sayidaty.net/",
    "https://www.syriamatrix.com/",
    "https://www.thaqfny.com/",
    "https://www.webteb.com/",
    "https://www.yallakora.com/",
    "https://www.yanba7.com/",
    "https://www.youm7.com/",
    "https://zawayan.com"
]

ARTICLE_LINK_SELECTORS = (
    "a.post-thumb::attr(href), "
    "a.post-link::attr(href), "
    "a.article-link::attr(href), "
    "a.entry-link::attr(href), "
    "a.news-link::attr(href), "
    "a.link::attr(href), "
    "a.item-link::attr(href), "
    "a.post::attr(href), "
    "a.headline-link::attr(href), "
    "a.read-more::attr(href), "
    "a.story-link::attr(href), "
    "a.content-link::attr(href), "
    "a.featured-link::attr(href), "
    "a.latest-link::attr(href), "
    "a[data-article-link]::attr(href), "
    "a[data-link]::attr(href), "
    "a.article::attr(href), "
    "a.title-link::attr(href), "
    "a.story::attr(href), "
    "a.blog-link::attr(href), "
    "a.feature-link::attr(href), "
    "a.external-link::attr(href), "
    "a.news-item::attr(href), "
    "a.content-item::attr(href), "
    "a.card-link::attr(href), "
    "a.primary-link::attr(href), "
    "a.secondary-link::attr(href), "
    "a.read-more-link::attr(href), "
    "a.teaser-link::attr(href), "
    "a.teaser-item::attr(href), "
    "a.link-article::attr(href), "
    "a.block-link::attr(href), "
    "a.article-title::attr(href), "
    "a.post-title::attr(href), "
    "a.story-title::attr(href), "
    "a.featured-story::attr(href), "
    "a[data-url]::attr(href), "
    "a[data-article]::attr(href)"
)

TITLE_SELECTORS = (
    "h1::text,"
    "h1.post-title::text,"
    "h1.article-title::text, "
    "h1.entry-title::text,"
    "h1.headline-title::text, "
    "h1.news-title::text, "
    "h1.title::text, "
    "h1.page-title::text, "
    "h2.post-title::text, "
    "h2.article-title::text, "
    "h2.entry-title::text, "
    "h2.headline-title::text, "
    "h2.news-title::text, "
    "h2.title::text, "
    "h2.page-title::text, "
    "h3.post-title::text, "
    "h3.article-title::text, "
    "h3.entry-title::text, "
    "h3.headline-title::text, "
    "h3.news-title::text, "
    "h3.title::text, "
    "h3.page-title::text, "
    "[data-article-title]::text, "
    "[data-title]::text"
)

LAST_UPDATED_SELECTORS = (
    "span.last-updated::text, "
    "span.time-updated::text, "
    "span.updated::text, "
    "span.date-updated::text, "
    "span.timestamp::text, "
    "span.publish-date::text, "
    "span.modified-date::text, "
    "span.post-date::text, "
    "span.published::text, "
    "span.pub-date::text, "
    "span.time::text, "
    "time::attr(datetime), "
    "time.updated::text, "
    "time.modified::text, "
    "time.posted-on::text, "
    "time.entry-date::text, "
    "time.date::text"
)

IMG_URL_SELECTORS = (
    "img.wp-post-image::attr(src), "
    "img.wp-post-image::attr(srcset), "
    "img.article-image::attr(src), "
    "img.featured-image::attr(src), "
    "img.main-image::attr(src), "
    "img.primary-image::attr(src), "
    "img.image::attr(src), "
    "img.post-image::attr(src), "
    "img.entry-image::attr(src), "
    "img.thumbnail::attr(src), "
    "img.header-image::attr(src), "
    "img.cover-image::attr(src), "
    "img.media-image::attr(src), "
    "img.picture::attr(src), "
    "img.photo::attr(src), "
    "img[data-src]::attr(data-src), "
    "img[data-lazy-src]::attr(data-lazy-src), "
    "img.lazyload::attr(data-src), "
    "img.lazy::attr(data-src)"
)

BODY_CONTENT_SELECTORS = (
    "div.entry-content p::text, "
    "div.entry-content ol::text, "
    "div.entry-content ul::text, "
    "div.entry-content h2::text, "
    "div.entry-content h3::text, "
    "div.entry-content h4::text, "
    "div.entry-content h5::text, "
    "div.entry-content h6::text, "
    "div.article-content p::text, "
    "div.article-content ol::text, "
    "div.article-content ul::text, "
    "div.article-content h2::text, "
    "div.article-content h3::text, "
    "div.article-content h4::text, "
    "div.article-content h5::text, "
    "div.article-content h6::text, "
    "div.content p::text, "
    "div.content ol::text, "
    "div.content ul::text, "
    "div.content h2::text, "
    "div.content h3::text, "
    "div.content h4::text, "
    "div.content h5::text, "
    "div.content h6::text, "
    "div.main-content p::text, "
    "div.main-content ol::text, "
    "div.main-content ul::text, "
    "div.main-content h2::text, "
    "div.main-content h3::text, "
    "div.main-content h4::text, "
    "div.main-content h5::text, "
    "div.main-content h6::text, "
    "div.post-content p::text, "
    "div.post-content ol::text, "
    "div.post-content ul::text, "
    "div.post-content h2::text, "
    "div.post-content h3::text, "
    "div.post-content h4::text, "
    "div.post-content h5::text, "
    "div.post-content h6::text"
)
