"""Unit test for Phase 3 profile-conditional branch classifier.

Guards the three decision paths:
  - `per_bullet` — bare-bullet exam spec
  - `strand_aggregated` — designed curriculum sources
  - `default` — unknown / empty profiles
"""

from __future__ import annotations

from curriculum_harness.phases.phase3_kud import _classify_profile_mode


def test_bare_bullet_exam_spec_selects_per_bullet() -> None:
    profile = {
        "document_family": "exam_specification",
        "scoping_strategy": "full_document",
        "assessment_signals": {
            "has_command_words": False,
            "has_mark_scheme": False,
        },
    }
    assert _classify_profile_mode(profile) == "per_bullet"


def test_exam_spec_with_command_words_selects_strand_aggregated() -> None:
    profile = {
        "document_family": "exam_specification",
        "scoping_strategy": "full_document",
        "assessment_signals": {
            "has_command_words": True,
            "has_mark_scheme": False,
        },
    }
    assert _classify_profile_mode(profile) == "strand_aggregated"


def test_exam_spec_with_mark_scheme_selects_strand_aggregated() -> None:
    profile = {
        "document_family": "exam_specification",
        "scoping_strategy": "full_document",
        "assessment_signals": {
            "has_command_words": False,
            "has_mark_scheme": True,
        },
    }
    assert _classify_profile_mode(profile) == "strand_aggregated"


def test_national_framework_selects_strand_aggregated() -> None:
    profile = {
        "document_family": "national_framework",
        "scoping_strategy": "grade_subject_filter",
        "assessment_signals": {},
    }
    assert _classify_profile_mode(profile) == "strand_aggregated"


def test_school_scoped_programme_selects_strand_aggregated() -> None:
    profile = {
        "document_family": "school_scoped_programme",
        "scoping_strategy": "grade_subject_filter",
        "assessment_signals": {},
    }
    assert _classify_profile_mode(profile) == "strand_aggregated"


def test_higher_ed_syllabus_selects_strand_aggregated() -> None:
    profile = {
        "document_family": "higher_ed_syllabus",
        "scoping_strategy": "full_document",
        "assessment_signals": {},
    }
    assert _classify_profile_mode(profile) == "strand_aggregated"


def test_empty_profile_selects_default() -> None:
    assert _classify_profile_mode({}) == "default"


def test_other_family_selects_default() -> None:
    profile = {
        "document_family": "other",
        "scoping_strategy": "grade_subject_filter",
        "assessment_signals": {},
    }
    assert _classify_profile_mode(profile) == "default"


def test_exam_spec_without_full_document_scope_selects_default() -> None:
    profile = {
        "document_family": "exam_specification",
        "scoping_strategy": "section_anchor",
        "assessment_signals": {
            "has_command_words": False,
            "has_mark_scheme": False,
        },
    }
    assert _classify_profile_mode(profile) == "default"
