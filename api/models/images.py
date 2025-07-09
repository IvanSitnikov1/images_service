from datetime import date

from sqlalchemy import Integer, String, Date, ForeignKey, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base


class Image(Base):
    __tablename__ = 'images'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    file_path: Mapped[str] = mapped_column(String)
    upload_date: Mapped[date] = mapped_column(Date, server_default=func.current_date())
    resolution: Mapped[str] = mapped_column(String)
    file_size: Mapped[int] = mapped_column(Integer)
    format: Mapped[str] = mapped_column(String)

    processed_images: Mapped[list['ProcessedImage']] = relationship(
        'ProcessedImage',
        back_populates='original_image',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )


class ProcessedImage(Base):
    __tablename__ = "processed_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_path: Mapped[str] = mapped_column(String)
    resolution: Mapped[str] = mapped_column(String)
    is_grayscale: Mapped[bool] = mapped_column(Boolean, default=False)

    original_image_id: Mapped[int] = mapped_column(ForeignKey('images.id', ondelete='CASCADE'))

    original_image: Mapped['Image'] = relationship(
        'Image',
        back_populates='processed_images',
    )
