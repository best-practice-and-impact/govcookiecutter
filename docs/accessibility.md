---
orphan: true
---
# Accessibility statement

This accessibility statement applies to content published on the
[best-practice-and-impact.github.io/govcookiecutter][github-pages] domain.

This website is run by the Office for National Statistics. We want as many people as
possible to be able to use this website. For example, that means you should be able to:

- change colours, contrast levels and fonts
- zoom in up to 300% without the text spilling off the screen
- navigate most of the website using just a keyboard
- navigate most of the website using speech recognition software
- listen to most of the website using a screen reader (including the most recent
  versions of JAWS, NVDA and VoiceOver)
- we've also made the website text as simple as possible to understand.

[AbilityNet][abilitynet] has advice on making your device easier to use if you have a
disability.

## How accessible this website is

We know some parts of this website are not fully accessible:

- some pages use layout tables rather than CSS tables.
- some links do not clearly explain where they lead, or that they lead to external
  sites.
- there are some external links to websites that may not be accessible.

## Feedback and contact information

If you need information on this website in a different format like accessible PDF,
large print, easy read, audio recording or braille:

- email [gsshelp@statistics.gov.uk][email]
- raise an issue on the [`govcookiecutter` GitHub repository][github-issues]

## Reporting accessibility problems with this website

We're always looking to improve the accessibility of this website. If you find any
problems not listed on this page or think we're not meeting accessibility requirements,
[email us][email], or [raise a GitHub issue][github-issues].

## Enforcement procedure

The Equality and Human Rights Commission (EHRC) is responsible for enforcing the Public
Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018
(the 'accessibility regulations'). If you're not happy with how we respond to your
complaint, [contact the Equality Advisory and Support Service (EASS)][eass].

## Technical information about this website's accessibility

The Office for National Statistics is committed to making its website accessible, in
accordance with the Public Sector Bodies (Websites and Mobile Applications) (No. 2)
Accessibility Regulations 2018.

## Compliance status

This website is partially compliant with the [Web Content Accessibility Guidelines
version 2.1][wcag] AA standard, due to the non-compliances listed below.

### Non-accessible content

The content listed below is non-accessible for the following reasons.

#### Non-compliance with the accessibility regulations

- Some pages use layout tables rather than CSS tables. This fails [WCAG 2.1 success
  criteria 1.3.1 Info and Relationships][wcag-2.1-1.3.1] and [1.3.2 Meaningful
  Sequence][wcag-2.1-1.3.2].
- Some links do not clearly explain where they lead, or that they lead to external
  sites. This fails [WCAG 2.1 success criteria 2.4.4 Link Purpose (In
  Context)][wcag-2.1-2.4.4].

#### Disproportionate burden

[The use of layout tables are due to the use of the
`sphinx.ext.autosummary`][sphinx-autosummary], and [`sphinx.ext.autodoc`
extensions][sphinx-autodoc]. This is a third-party, open source code base, and so is
beyond the scope of this project to fix, although we will apply updates as this
codebase develops.

#### Content that's not within the scope of the accessibility regulations

The [Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility
Regulations 2018 legislation][accessibility-legislation] does not require us to fix
external, third-party websites that are neither funded nor developed by, nor under the
control of the Office for National Statistics (ONS).

## How we tested this website

The test was carried out by the data science team at the Government Digital Service
(GDS). They used the [WAVE Web Accessibility Evaluation Tool][wave] and a checklist
created by the GDS technical writing team with help from the GDS accessibility team.
They tested all pages on this site.

## What we're doing to improve accessibility

We plan to fix the accessibility issues in the content by the end of December 2021.

## Preparation of this accessibility statement

This statement was prepared on 30 June 2021. It was last reviewed on 20 July 2021.

[abilitynet]: https://abilitynet.org.uk/
[accessibility-legislation]: https://www.legislation.gov.uk/uksi/2018/952/regulation/4/made
[eass]: https://www.equalityadvisoryservice.com/
[email]: mailto:gsshelp@statistics.gov.uk
[github-issues]: https://github.com/best-practice-and-impact/govcookiecutter/issues/new
[github-pages]: https://best-practice-and-impact.github.io/govcookiecutter
[sphinx-autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[sphinx-autosummary]: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[wave]: https://wave.webaim.org/
[wcag]: https://www.w3.org/TR/WCAG21/
[wcag-2.1-1.3.1]: https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html
[wcag-2.1-1.3.2]: https://www.w3.org/TR/UNDERSTANDING-WCAG20/content-structure-separation-sequence.html
[wcag-2.1-2.4.4]: https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html
