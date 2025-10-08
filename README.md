# indexer
Indexer is a Python-based indexer designed for analyzing and organizing large, heterogeneous datasets. It can process entire directories containing videos, audio files, images, text documents, and PDFs.
It is still under development.




Main Features
Full-text and metadata search across all indexed content
Speech recognition for audio and video files
Object and scene detection in images and videos
Text and OCR extraction from documents and images
PDF analysis including embedded text and images
Web interface for browsing, searching, and previewing results
Support for large-scale datasets and incremental indexing
Modular architecture with easily extendable extractors and backends
Supported File Types
Video/Audio: mp4, mkv, mov, mp3, wav, flac
Images: jpg, png, tiff, webp
Documents: txt, pdf, md, docx (optional conversion)
Directories/Archives: recursive folder scanning
Architecture Overview
Crawler – scans folders, gathers file metadata and hashes
Dispatcher – assigns files to the appropriate extractors
Extractors – process files depending on type:
Video/Audio: uses FFmpeg for segmentation and analysis, then applies speech recognition and optional object detection
Images: applies object detection, OCR, and metadata extraction
Text/PDF: parses content and performs OCR if necessary
Normalizer – unifies metadata formats
Indexer – stores results in a searchable database or search engine
API and Web UI – provide endpoints and an interactive interface for exploration and querying
System Requirements
Python 3.10 or higher
FFmpeg installed and available in the system path
Optional: Tesseract for OCR, CUDA for GPU acceleration

