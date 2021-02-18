import pytest

from openflow.openflow import get_part


@pytest.mark.parametrize(
    'part, name, family, device, package', [
        ('hx8k-ct256', 'hx8k-ct256', 'ice40', 'hx8k', 'ct256'),
        ('HX8K-CT256', 'hx8k-ct256', 'ice40', 'hx8k', 'ct256'),
        ('hx4k-tq144', 'hx4k-tq144', 'ice40', 'hx8k', 'tq144:4k'),
        ('25k-CSFBGA285', '25k-csfbga285', 'ecp5', '25k', 'csfbga285'),
        ('um5g-85k-CABGA381', 'um5g-85k-cabga381', 'ecp5', 'um5g-85k', 'cabga381')
    ]
)
def test_part(part, name, family, device, package):
    result = get_part(part)
    print(result)
    assert result['name'] == name
    assert result['family'] == family
    assert result['device'] == device
    assert result['package'] == package

