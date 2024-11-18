"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import services using HelloWorld naming convention
from .orders.CarService import CarService
from .orders.CarImageService import CarImageService
from .orders.TimeSlotService import TimeSlotService
from .orders.FeedbackService import FeedbackService
from .orders.BrandService import BrandService
from .orders.TestDriveService import TestDriveService
from .orders.SellerService import SellerService
from .orders.EngineService import EngineService
from .orders.ModelService import ModelService
from .orders.LocationService import LocationService
from .orders.UserService import UserService
from .orders.CompanyService import CompanyService

# Initialize service instances
carService = CarService()
carImageService = CarImageService()
timeSlotService = TimeSlotService()
feedbackService = FeedbackService()
brandService = BrandService()
testDriveService = TestDriveService()
sellerService = SellerService()
engineService = EngineService()
modelService = ModelService()
locationService = LocationService()
userService = UserService()
companyService = CompanyService()
