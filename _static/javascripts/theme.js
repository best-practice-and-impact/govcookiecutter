// Sets `sphinx.ext.autosummary` table columns to 50%:50%, which looks nicer
$(function() {
    $('table.longtable > colgroup').find('col').each(function() {
        $(this).css('width', '50%');
    });
});

// Sets the correct link for the anchored heading icon
$(function() {
    $('section').find('h1.anchored-heading, h2.anchored-heading, h3.anchored-heading, h4.anchored-heading, h5.anchored-heading, h6.anchored-heading').each(function() {
        $(this).find('a.anchored-heading__icon').attr('href', '#' + $(this).parents('section').attr('id'));
    });
});

// Sets the `aria-hidden` attribute for the GOV.UK Design System warning text, and allows for multiline text. This is
// generated using the `warning` directive created using the `WarningText` class
$(function() {
    $('div.govuk-warning-text.docutils.container').each(function() {
        $(this).find('span.govuk-warning-text__icon').attr('aria-hidden', 'true');
        $(this).find('strong.govuk-warning-text__text').css('white-space', 'pre-wrap');
    });
});

// Sets attributes, styles, and link classes for the GOV.UK Design System notification banner. This is generated using
// the `note` directive created using the `NotificationBanner` class
$(function() {
    $('div.govuk-notification-banner.docutils.container').each(function() {
        $(this).attr({role: 'region', 'aria-labelledby': 'govuk-notification-banner-title',
                      'data-module': 'govuk-notification-banner'});
        $(this).find('h2.govuk-notification-banner__title.anchored-heading > a.anchored-heading__icon').css('display', 'none');
        $(this).find('p.govuk-notification-banner__heading').css('white-space', 'pre-wrap');
        $(this).find('p.govuk-notification-banner__heading > a').addClass('govuk-notification-banner__link')
    });
});

// Remove Sphinx pilcrow header links - these already exist in the GOV.UK Tech Docs template
$(function() {
    $('a.headerlink').filter(function() {
        return $(this).text() == '¶';
    }).remove();
});

// Wrap internal links
$(function() {
    $('a.reference.internal').each(function() {
        $(this).css('overflow-wrap', 'break-word');
        $(this).css('word-wrap', 'break-word');
    });
});
