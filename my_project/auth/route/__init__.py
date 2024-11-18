"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.UserBlueprint import user_bp
    from .orders.CompanyBlueprint import company_bp
    from .orders.TestDriveBlueprint import testdrive_bp
    from .orders.SellerBlueprint import seller_bp
    from .orders.BrandBlueprint import brand_bp
    from .orders.EngineBlueprint import engine_bp
    from .orders.TimeSlotBlueprint import timeslot_bp
    from .orders.CarBlueprint import car_bp
    from .orders.ModelBlueprint import model_bp
    from .orders.LocationBlueprint import location_bp
    from .orders.FeedbackBlueprint import feedback_bp
    from .orders.CarImageBlueprint import carimage_bp

    # Register each blueprint with the app
    app.register_blueprint(user_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(testdrive_bp)
    app.register_blueprint(seller_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(engine_bp)
    app.register_blueprint(timeslot_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(model_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(carimage_bp)
