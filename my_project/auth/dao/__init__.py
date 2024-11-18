"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.CarDAO import CarDAO
from .orders.TimeSlotDAO import TimeSlotDAO
from .orders.FeedbackDAO import FeedbackDAO
from .orders.CarImageDAO import CarImageDAO
from .orders.BrandDAO import BrandDAO
from .orders.EngineDAO import EngineDAO
from .orders.UserDAO import UserDAO
from .orders.ModelDAO import ModelDAO
from .orders.LocationDAO import LocationDAO
from .orders.TestDriveDAO import TestDriveDAO
from .orders.CompanyDAO import CompanyDAO
from .orders.SellerDAO import SellerDAO

carDao = CarDAO()
timeSlotDao = TimeSlotDAO()
feedbackDao = FeedbackDAO()
carImageDao = CarImageDAO()
brandDao = BrandDAO()
engineDao = EngineDAO()
userDao = UserDAO()
modelDao = ModelDAO()
locationDao = LocationDAO()
testDriveDao = TestDriveDAO()
companyDao = CompanyDAO()
sellerDao = SellerDAO()