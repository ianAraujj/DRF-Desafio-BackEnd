from regular_plan.models import RegularPlan
from django.contrib.auth.models import User

def insertSeeds():

    user1 = User.objects.create_user(
        'john', 'lennon@thebeatles.com', 'johnpassword'
    )

    user2 = User.objects.create_user(
        'paul', 'McCartney@thebeatles.com', 'johnpassword'
    )

    user3 = User.objects.create_user(
        'george', 'harrison@thebeatles.com', 'johnpassword'
    )

    user4 = User.objects.create_user(
        'ringo', 'star@thebeatles.com', 'johnpassword'
    )

    
    RegularPlan.objects.create(
        name='Test 1',
        tar_included=True,
        subscription=90,
        cycle='Weekly',
        type='Tri-Time',
        offer_iva=False,
        off_peak_price=2,
        peak_price=5,
        unit='min',
        valid=True,
        publish=True,
        vat=90,
        owner=user1
    )

    RegularPlan.objects.create(
        name='Test 2',
        tar_included=False,
        subscription=180,
        cycle='Daily',
        type='Simple',
        offer_iva=False,
        off_peak_price=4,
        peak_price=5,
        unit='min',
        valid=True,
        publish=True,
        vat=40,
        owner=user2
    )

    RegularPlan.objects.create(
        name='Test 3',
        tar_included=True,
        subscription=200,
        cycle='Daily',
        type='Bi-Time',
        offer_iva=False,
        off_peak_price=1,
        peak_price=2,
        unit='min',
        valid=True,
        publish=True,
        vat=20,
        owner=user3
    )

    RegularPlan.objects.create(
        name='Test 4',
        tar_included=True,
        subscription=90,
        cycle='Daily',
        type='Bi-Time',
        offer_iva=False,
        off_peak_price=20,
        peak_price=35,
        unit='min',
        valid=True,
        publish=True,
        vat=10,
        owner=user4
    )

    RegularPlan.objects.create(
        name='Test 5',
        tar_included=False,
        subscription=40,
        cycle='Weekly',
        type='Simple',
        offer_iva=False,
        off_peak_price=2,
        peak_price=5,
        unit='min',
        valid=True,
        publish=True,
        vat=20,
        owner=user1
    )

    RegularPlan.objects.create(
        name='Test 6',
        tar_included=True,
        subscription=90,
        cycle='Weekly',
        type='Bi-Time',
        offer_iva=False,
        off_peak_price=1,
        peak_price=5,
        unit='min',
        valid=False,
        publish=False,
        vat=90,
    )

    RegularPlan.objects.create(
        name='Test 7',
        tar_included=True,
        subscription=130,
        cycle='Daily',
        type='Simple',
        offer_iva=False,
        off_peak_price=5,
        peak_price=5,
        unit='min',
        valid=False,
        publish=False,
        vat=20,
    )