from django.db import models
from services.models import Service


class VideoService(models.Model):
    """
    model: VideoService луги по подключению Видеонаблюдения
    """

    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Услуга по Видеонаблюдению"
        verbose_name_plural = "Услуги по Видеонаблюдению"


TRANSFER_TYPE = [
    ("ANALOG", "Аналоговая камера"),
    ("DIGITAL", "Цифровая камера"),
]


class Camera(models.Model):
    """
        model: Camera (Камера)

    resolution_in_mp (int) - Разрешение в МП
    angel_view (int) - Угол обзора

    data_transfer_type (text choice) - Тип передачи данных (аналог / цифра)

    motion_detection (bool) - Обнаружение движения
    night_vision(bool) - Ночное видение
    weather_proof(bool) - Защита от непогоды
    sound_recording (bool) - запись звука
    optical_zoom (bool) - оптический зум
    colorVu (bool) -  Наличие технологии  ColorVu
    PTZ_camera (bool) - Наличие системы приводов для поворота, наклона и зумирования

    """

    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    resolution_in_mp = models.IntegerField(null=True, blank=True, verbose_name="Разрешение в МП")
    angel_view = models.IntegerField(null=True, blank=True, verbose_name="Угол обзора")

    data_transfer_type = models.CharField(
        max_length=7,
        choices=TRANSFER_TYPE,
        default="DIGITAL",
        verbose_name="Тип камеры",
        help_text="Цифровая / Аналоговая камера",
    )

    motion_detection = models.BooleanField(
        default=True, verbose_name="Обнаружение движения", help_text="Наличие функции motion_detection"
    )
    night_vision = models.BooleanField(
        default=True, verbose_name="Ночное видение", help_text="Наличие съемки в темноте"
    )
    weather_proof = models.BooleanField(
        default=True,
        verbose_name="Защита от непогоды",
        help_text="Наличие weather_proof, возможность установки на улице",
    )
    sound_recording = models.BooleanField(default=True, verbose_name="Запись звука", help_text="Наличие записи звука")
    optical_zoom = models.BooleanField(
        default=True, verbose_name="Оптический зум", help_text="Наличие оптического зума"
    )
    colorVu = models.BooleanField(default=True, verbose_name="ColorVu", help_text="Наличие технологии  ColorVu")
    PTZ_camera = models.BooleanField(
        default=True,
        verbose_name="PTZ_camera",
        help_text="Наличие системы приводов для поворота, наклона и зумирования",
    )
    base_service = models.ManyToManyField(
        VideoService, related_name="cameras", blank=True, verbose_name="Обязательные услуги"
    )
    available = models.BooleanField(default=True, verbose_name="Есть ли в наличии")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Камера"
        verbose_name_plural = "Камеры"


class CameraSystem(models.Model):
    """
        model: NVR_camera_system (Сетовой видеорегистратор)

    hdd_included (bool) - Наличие жесткого диска в комплекте
    hdd_included_size (int) - Объем жесткого диска в комплекте (default = 0)
    max_hdd_size_gb (int) - Максимальный размер жесткого диска

    ports_quantity_for_analog_cameras (int) - Кол-во портов для аналоговых камер
    ports_quantity_for_digital_cameras (int) - Кол-во портов для цифровых камер
    max_ports_quantity_for_analog_cameras (int) - Максимально кол-во портов для аналоговых камер
    max_ports_quantity_for_digital_cameras (int) - Максимально кол-во портов для цифровых камер
    motion_detection_ports_quantity (int) - Кол-во портов поддерживающих обнаружение движения
    acusense_ports_quantity (int) - Кол-во портов поддерживающих технологиею AcuSense (распознавание лиц)
    """

    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    hdd_included = models.BooleanField(default=False, verbose_name="Наличие жесткого диска в комплекте")
    hdd_included_size_gb = models.IntegerField(default=0, verbose_name="Объем жесткого диска в комплекте")
    max_hdd_size_gb = models.IntegerField(null=True, blank=True, verbose_name="Максимальный размер жесткого диска")
    ports_quantity_for_analog_cameras = models.IntegerField(verbose_name="Кол-во портов для аналоговых камер")
    ports_quantity_for_digital_cameras = models.IntegerField(verbose_name="Кол-во портов для цифровых камер")
    max_ports_quantity_for_analog_cameras = models.IntegerField(
        verbose_name="Максимально кол-во портов для аналоговых камер"
    )
    max_ports_quantity_for_digital_cameras = models.IntegerField(
        verbose_name="Максимально кол-во портов для цифровых камер"
    )
    motion_detection_ports_quantity = models.IntegerField(
        verbose_name="Кол-во портов поддерживающих обнаружение движения"
    )
    acusense_ports_quantity = models.IntegerField(
        verbose_name="Кол-во портов поддерживающих технологиею AcuSense (распознавание лиц)"
    )
    base_service = models.ManyToManyField(
        VideoService, related_name="camera_systems", blank=True, verbose_name="Обязательные услуги"
    )
    available = models.BooleanField(default=True, verbose_name="Есть ли в наличии")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Сетовой видеорегистратор"
        verbose_name_plural = "Сетовыу видеорегистраторы"


class HDD(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    size_gb = models.IntegerField(verbose_name="Объем жесткого диска в ГБ")
    base_service = models.ManyToManyField(
        VideoService, related_name="hdds", blank=True, verbose_name="Обязательные услуги"
    )
    available = models.BooleanField(default=True, verbose_name="Есть ли в наличии")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Жесткий диск"
        verbose_name_plural = "Жесткие диски"
