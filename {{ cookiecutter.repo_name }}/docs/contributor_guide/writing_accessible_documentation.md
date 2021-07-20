# Writing accessible documentation

[You can build this project's documentation into a website using
Sphinx][docs-write-sphinx-documentation]. If you work in the public sector, and build a
website, by law the website must be accessible.

The full name of the accessibility regulations is the Public Sector Bodies (Websites
and Mobile Applications) (No. 2) Accessibility Regulations 2018.

It came into force on 23 September 2018, and all public sector bodies have to meet
these requirements unless exempt. [GOV.UK has further details to help you understand
the impact of the 2018 requirements][govuk-accessibility]

We use the following checklist to determine how accessible our documentation is, when
rendered as a website using Sphinx.

- [check the website against the WAVE Web Accessibility Evaluation Tool][wave]
- check that link text is descriptive
- check the hierarchy of page headings, which should go in order from `h2` to `h4` with
  no gaps
- remove italics, and bold text
- only use block capitals inside curly braces for placeholders in code examples
- check for accessible language
  - use [`alex.js` to identify insensitive, and inconsiderate writing][alex-js]
  - replace instances of `click` with `select` or `choose`
  - remove latin phrases (`e.g.`, `i.e.`, `ad hoc`, `via`)
  - [use GOV.UK inclusive language][govuk-language]
  - [replace negative contractions][negative-contractions]
  - aim not to have long sentences (maximum 25 words per sentence)
  - aim not to have long paragraphs (maximum 5 lines per paragraph)
  - check for unique titles in documentation
  - check diagrams and images for alternative text as well as surrounding contextual
    text
  - remove diagrams/images that do not add anything to a user's understanding
  - remove screenshots if possible
  - [use accessible SVGs][govuk-design-system-images]
  - [check for inaccessible formats][govuk-accessible-formats]

This checklist was created by the Government Digital Service (GDS) technical writing
team with help from the GDS accessibility team. We then [draft a suitable accessibility
statement for the project; an example is available on
GOV.UK][govuk-sample-accessibility].

[alex-js]: https://alexjs.com/
[docs-write-sphinx-documentation]: ./writing_sphinx_documentation.md
[govuk-accessible-formats]: https://www.gov.uk/guidance/how-to-publish-on-gov-uk/accessible-pdfs
[govuk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
[govuk-design-system-images]: https://design-system.service.gov.uk/styles/images/
[govuk-language]: https://www.gov.uk/government/publications/inclusive-communication/inclusive-language-words-to-use-and-avoid-when-writing-about-disability
[govuk-sample-accessibility]: https://www.gov.uk/government/publications/sample-accessibility-statement
[negative-contractions]: https://www.englishclub.com/vocabulary/contractions-negative.htm
[wave]: https://wave.webaim.org/
