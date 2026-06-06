#!/usr/bin/env python3
"""Split the master Bengali AI book into per-chapter .docx files."""

import copy
import os
import re
from docx import Document
from docx.oxml.ns import qn

MASTER = "এআই_কীভাবে_সিদ্ধান্ত_নেয়_Bengali.docx"
OUT_DIR = "chapters"

def get_style_id(para):
    pPr = para._element.find(qn('w:pPr'))
    if pPr is None:
        return None
    pStyle = pPr.find(qn('w:pStyle'))
    if pStyle is None:
        return None
    return pStyle.get(qn('w:val'))

def sanitize_filename(text, max_len=40):
    clean = re.sub(r'[\\/:*?"<>|]', '', text).strip()
    clean = re.sub(r'\s+', '_', clean)
    return clean[:max_len]

def copy_styles(src_doc, dst_doc):
    """Copy all style definitions from source to destination."""
    src_styles = src_doc.element.find(qn('w:styles'))
    if src_styles is not None:
        dst_styles = dst_doc.element.find(qn('w:styles'))
        if dst_styles is not None:
            dst_styles.getparent().remove(dst_styles)
        dst_doc.element.insert(0, copy.deepcopy(src_styles))

def copy_section_props(src_doc, dst_doc):
    """Copy page size and margins from source to destination."""
    src_section = src_doc.sections[0]
    dst_section = dst_doc.sections[0]
    dst_section.page_width = src_section.page_width
    dst_section.page_height = src_section.page_height
    dst_section.top_margin = src_section.top_margin
    dst_section.bottom_margin = src_section.bottom_margin
    dst_section.left_margin = src_section.left_margin
    dst_section.right_margin = src_section.right_margin

def create_chapter_doc(src_doc, paragraphs, filename):
    """Create a new docx with the given paragraphs, preserving formatting."""
    dst_doc = Document()
    copy_styles(src_doc, dst_doc)
    copy_section_props(src_doc, dst_doc)

    body = dst_doc.element.body
    default_para = body.find(qn('w:p'))
    if default_para is not None:
        body.remove(default_para)

    for para in paragraphs:
        new_elem = copy.deepcopy(para._element)
        body.append(new_elem)

    path = os.path.join(OUT_DIR, filename)
    dst_doc.save(path)
    return path

def main():
    doc = Document(MASTER)
    all_paras = doc.paragraphs

    toc_styles = {'TOC1', 'TOC2', 'TOC3', 'TOC4', 'TOC5'}
    first_content_idx = None
    for i, p in enumerate(all_paras):
        sid = get_style_id(p)
        if sid == 'Title':
            first_content_idx = i
            break

    if first_content_idx is None:
        print("ERROR: Could not find Title paragraph")
        return

    heading1_indices = []
    for i in range(first_content_idx, len(all_paras)):
        if get_style_id(all_paras[i]) == 'Heading1':
            heading1_indices.append(i)

    title_paras = all_paras[first_content_idx:heading1_indices[0]]
    title_file = create_chapter_doc(doc, title_paras, "00_title.docx")
    print(f"Created: {title_file} ({len(title_paras)} paragraphs)")

    for ch_num, start_idx in enumerate(heading1_indices, 1):
        if ch_num < len(heading1_indices):
            end_idx = heading1_indices[ch_num]
        else:
            end_idx = len(all_paras)

        chapter_paras = all_paras[start_idx:end_idx]
        chapter_title = all_paras[start_idx].text.strip()
        short_title = sanitize_filename(chapter_title)
        filename = f"{ch_num:02d}_{short_title}.docx"

        path = create_chapter_doc(doc, chapter_paras, filename)
        print(f"Created: {path} ({len(chapter_paras)} paragraphs)")

    print(f"\nDone! {len(heading1_indices) + 1} files in {OUT_DIR}/")

if __name__ == "__main__":
    main()
