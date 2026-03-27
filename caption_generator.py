"""
Caption Generator — marketing-style captions based on a campaign name and aura.

Supported auras
---------------
SPARK  → energetic
FROST  → minimal / precise
VOID   → mysterious
"""

AURAS = {
    "SPARK": "energetic",
    "FROST": "minimal / precise",
    "VOID": "mysterious",
}

_TEMPLATES = {
    "SPARK": [
        "🔥 {name} is here to ignite everything you thought possible. Are you ready?",
        "⚡ Unleash the energy. {name} — feel the spark and never look back.",
        "🚀 The future is loud, bold, and unstoppable. Welcome to {name}.",
    ],
    "FROST": [
        "{name}. Refined. Relentless.",
        "Clarity over noise. {name} — nothing more, nothing less.",
        "Precision at every step. That's {name}.",
    ],
    "VOID": [
        "Some things exist between the lines. {name} is one of them.",
        "🌑 Not everything needs to be explained. {name} speaks in silence.",
        "Step into the unknown. {name} — where the ordinary disappears.",
    ],
}


def generate_captions(name: str, aura: str) -> list[str]:
    """Return 3 marketing caption variations for *name* based on *aura*.

    Parameters
    ----------
    name:
        The campaign name to feature in the captions.
    aura:
        One of ``"SPARK"``, ``"FROST"``, or ``"VOID"`` (case-insensitive).

    Returns
    -------
    list[str]
        A list of exactly 3 caption strings.

    Raises
    ------
    ValueError
        If *aura* is not one of the supported values.
    """
    aura_key = aura.upper()
    if aura_key not in _TEMPLATES:
        supported = ", ".join(AURAS.keys())
        raise ValueError(
            f"Unknown aura '{aura}'. Supported auras: {supported}."
        )

    return [template.format(name=name) for template in _TEMPLATES[aura_key]]


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python caption_generator.py <campaign_name> <aura>")
        print(f"Available auras: {', '.join(AURAS.keys())}")
        sys.exit(1)

    campaign, selected_aura = sys.argv[1], sys.argv[2]
    try:
        captions = generate_captions(campaign, selected_aura)
        aura_label = AURAS[selected_aura.upper()]
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print(f'\nCaptions for "{campaign}" [{selected_aura.upper()} — {aura_label}]\n')
    for i, caption in enumerate(captions, 1):
        print(f"  {i}. {caption}")
    print()
