# encoding: utf-8

from statics import equals
from statics import rounded
from statics import vector_length


def unitize(lista, rev):
    """
    Allinea gli elementi in base ai punti inizio e fine
    param lista: list: elementi da allineare
    param rev: boolean: ordinamento inverso
    return: elementi allineati
    """
    elem_count = 0
    ordered = list()
    disordered = lista[:]
    if len(disordered) == 0:
        pass
    elif len(disordered) == 1:
        ordered.append(disordered[0])
        elem_count += 1
    else:
        keypoint = [0, 0] if rev else [15, 6]
        span = first_span(disordered, keypoint)
        while span:
            keypoint = rounded(span.end)
            ordered.append(span)
            disordered.remove(span)
            span = next_span(disordered, span)

        while len(disordered) > 0:
            span = first_span(disordered, keypoint)
            elem_count += 1
            while span:
                keypoint = rounded(span.end)
                ordered.append(span)
                disordered.remove(span)
                span = next_span(disordered, span)

    return ordered, elem_count


def first_span(disordered, keypoint):
    """
    Individua il segmento iniziale (il più vicino al keypoint)
    param disordered: lista dei segmenti da allineare
    return: segmento iniziale
    """
    if len(disordered) == 1:
        if vector_length(keypoint, disordered[0].start) > vector_length(keypoint, disordered[0].end):
            disordered[0].reverse()
        return disordered[0]

    points = unique_points(disordered)

    if not points:
        return disordered[0]

    minimum = 999.0
    nearest_point = None
    for point in points:
        distance = vector_length(keypoint, point)
        if distance < minimum:
            minimum = distance
            nearest_point = point

    for line in disordered:
        if equals(nearest_point, line.start):
            return line
        if equals(nearest_point, line.end):
            line.reverse()
            return line


def next_span(disordered, test_span):
    """
    Individua il segmento successivo tangente all'ultimo segmento allineato
    param disordered: lista dei segmenti da allineare
    param test_span: ultimo segmento allineato
    return: segmento tangente successivo
    """
    for line in disordered:
        if equals(test_span.end, line.start):
            return line
        if equals(test_span.end, line.end):
            line.reverse()
            return line
    return None


def unique_points(disordered):
    points = [rounded(line.start) for line in disordered]
    points.extend([rounded(line.end) for line in disordered if not line.is_closed])
    uni_points = [pt for pt in points if points.count(pt) == 1]
    return uni_points  # if len(unique_points) == 2 else points
