from discount_service import DiscountService
from diwali import DiwaliStrategy
from holi import HoliStrategy


diwali_strategy = DiwaliStrategy()
holi_strategy = HoliStrategy()

ds = DiscountService(diwali_strategy)
ds.process()

print("----------------------------")

ds.set_strategy(holi_strategy)
ds.process()