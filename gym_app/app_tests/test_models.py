from django.test import TestCase
from gym_app.models import Member, Plan
from datetime import date

class PlanModelTest(TestCase):
    def test_plan_creation(self):
        plan = Plan.objects.create(name="Gold", duration_months=6, price=500)
        self.assertEqual(plan.name, "Gold")
        self.assertEqual(plan.duration_months, 6)
        self.assertEqual(plan.price, 500)
        self.assertTrue(plan.is_active)
        self.assertEqual(str(plan), "Gold - ₹500")

class MemberModelTest(TestCase):
    def test_member_creation(self):
        plan = Plan.objects.create(name="Silver", duration_months=3, price=300)
        member = Member.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="john@example.com",
            plan=plan
        )
        self.assertEqual(member.first_name, "John")
        self.assertEqual(member.last_name, "Doe")
        self.assertEqual(member.email, "john@example.com")
        self.assertEqual(member.plan, plan)
        self.assertTrue(member.is_active)
        self.assertEqual(str(member), "John Doe")
