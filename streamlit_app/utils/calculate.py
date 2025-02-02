import math

def calculate(circ):
    try:
        circ = float(circ)
    except ValueError:
        return "The circumference must be a number between 1 and 1000."
    
    if circ < 1 or circ > 1000:
        return f"The circumference must be a number between 1 and 1000: {circ}"
    
    # C10 Calculations
    triside = math.asin(2 / math.sqrt(10 + 2 * math.sqrt(5)))
    pentside = math.asin(2 / ((math.sqrt(5) + 1) * math.sqrt(3)))
    a = circ * triside / math.pi
    b = circ * pentside / math.pi
    c = circ * math.acos(math.cos(triside) * math.cos(pentside)) / (2 * math.pi)
    a1, b1, c1 = round(a, 2), round(b, 2), round(c, 2)
    d1, f1 = round(a / 2, 2), round(b / 2, 2)
    
    c10_results = (
        f"<ol><li>triangle side (C10 number) = {a1} cm</li>"
        f"<li>pentagon side = {b1} cm</li>"
        f"<li>diamond side = {c1} cm</li>"
        f"<li>short line in pentagon = long line in diamond = {d1} cm</li>"
        f"<li>long line in pentagon = long line in triangle = {c1} cm</li>"
        f"<li>short line of triangle = short line in diamond = {f1} cm</li></ol>"
    )
    
    # C8 Calculations
    triside = math.asin(1 / math.sqrt(2))
    squareside = math.asin(1 / math.sqrt(3))
    a = circ * triside / math.pi
    b = circ * squareside / math.pi
    c = circ * math.acos(math.cos(triside) * math.cos(squareside)) / (2 * math.pi)
    d = circ * math.asin(2 / math.sqrt(6)) / math.pi
    a1, b1, c1, d1 = round(a, 2), round(b, 2), round(c, 2), round(d, 2)
    e1, f1, g1 = round(a / 2, 2), round(c, 2), round(b / 2, 2)
    
    c8_results = (
        f"<ol><li>6-part triangle side = {a1} cm</li>"
        f"<li>square side = {b1} cm</li>"
        f"<li>diamond side = {c1} cm</li>"
        f"<li>12-part triangle side = {d1} cm</li>"
        f"<li>short line in square = long line in diamond = {e1} cm</li>"
        f"<li>long line of square = long line of 6-part triangle = {f1} cm</li>"
        f"<li>short line in 6-part triangle = short line of diamond = {g1} cm</li></ol>"
    )
    
    # C6 Calculations
    c1 = round(d / 2, 2)
    
    c6_results = (
        f"<ol><li>square side (C6 number) = {b1} cm</li>"
        f"<li>6-part triangle (tetrahedral) side = {d1} cm</li>"
        f"<li>short line of tetrahedral triangle = {c1} cm</li>"
        f"<li>long line of tetrahedral triangle  = {b1} cm</li></ol>"
    )
    
    return {
        "c10_results": c10_results,
        "c8_results": c8_results,
        "c6_results": c6_results
    }
    