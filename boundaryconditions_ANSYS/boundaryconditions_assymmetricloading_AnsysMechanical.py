def after_geometry_changed(this, geometry_object):# Do not edit this line
    """
    Called after geometry has been changed.
    Keyword Arguments : 
        this -- the datamodel object instance of the python code object you are currently editing in the tree
        geometry_object -- The geometry
    """
    

    # To access properties created using the Property Provider, please use the following command.
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name")

    # To access scoping properties use the following to access geometry scoping and named selection respectively:
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name/Geometry Selection")
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name/Named Selection")
    # Loop in reverse to avoid modifying the list while iterating
    
    
    Material1 = 'glass'
    Material2 = 'interlayer'
    glass_ids = []
    interlayer_ids = []
    # Get all bodies in the model
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)
    for i, body in enumerate(all_bodies):
        # Assign materials
        if i <= 44:
            body.Material = Material2
            geo_body = body.GetGeoBody()
            glass_ids.append(geo_body.Id)
        else:
            body.Material = Material1
            geo_body = body.GetGeoBody()
            interlayer_ids.append(geo_body.Id)
    
    named_selections = ExtAPI.DataModel.Project.Model.NamedSelections
    sel_glass = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_glass.Ids = glass_ids
    glass_named = named_selections.Children[1]
    glass_named.ScopingMethod = GeometryDefineByType.Geometry
    glass_named.Location = sel_glass
    
    # Create Named Selection for interlayer bodies
    sel_inter = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_inter.Ids = interlayer_ids
    inter_named = named_selections.Children[0]
    inter_named.ScopingMethod = GeometryDefineByType.Geometry
    inter_named.Location = sel_inter

    ###PRESSURE C
    target_face_ids = []
    special_face5_indices = {45, 46, 50, 51, 55, 56}
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)

    for i in range(45, 57):  # 57 is exclusive
        body = all_bodies[i]
        geo_body = body.GetGeoBody()
    
        face_index = 5 if i in special_face5_indices else 2
        if len(geo_body.Faces) > face_index:
            target_face_ids.append(geo_body.Faces[face_index].Id)

    # Assign to named_selections.Children[6]
    sel_info = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_info.Ids = target_face_ids
    named_selections.Children[6].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[6].Location = sel_info
    
    #PRESSURE B
    target_face_ids = []
    special_face5_indices = {60, 61, 65, 66, 70, 71, 75, 76}
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)

    for i in range(57, 80):  # 80 is exclusive
        body = all_bodies[i]
        geo_body = body.GetGeoBody()
    
        face_index = 5 if i in special_face5_indices else 2
        if len(geo_body.Faces) > face_index:
            target_face_ids.append(geo_body.Faces[face_index].Id)

    # Assign to named_selections.Children[6]
    sel_info = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_info.Ids = target_face_ids
    named_selections.Children[5].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[5].Location = sel_info
    
    #PRESSURE A
    target_face_ids = []
    special_face5_indices = {80, 81, 85, 86, 90, 91}
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)

    for i in range(80, 92):  # 80 is exclusive
        body = all_bodies[i]
        geo_body = body.GetGeoBody()
    
        face_index = 5 if i in special_face5_indices else 2
        if len(geo_body.Faces) > face_index:
            target_face_ids.append(geo_body.Faces[face_index].Id)

    # Assign to named_selections.Children[6]
    sel_info = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_info.Ids = target_face_ids
    named_selections.Children[4].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[4].Location = sel_info
    
    
    ###all external faces
    target_face_ids = []
    special_face5_indices = {45, 46, 50, 51, 55, 56, 60, 61, 65, 66, 70, 71, 75, 76, 80, 81, 85, 86, 90, 91}
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)

    for i in range(45, 92):  # 80 is exclusive
        body = all_bodies[i]
        geo_body = body.GetGeoBody()
    
        face_index = 5 if i in special_face5_indices else 2
        if len(geo_body.Faces) > face_index:
            target_face_ids.append(geo_body.Faces[face_index].Id)

    # Assign to named_selections.Children[6]
    sel_info = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_info.Ids = target_face_ids
    named_selections.Children[8].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[8].Location = sel_info
    
    #PRESSURE Point
    target_face_ids = []
    special_face5_indices = {67, 68, 69}
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)

    for i in range(67, 70):  # 80 is exclusive
        body = all_bodies[i]
        geo_body = body.GetGeoBody()
    
        face_index = 2
        if len(geo_body.Faces) > face_index:
            target_face_ids.append(geo_body.Faces[face_index].Id)

    # Assign to named_selections.Children[6]
    sel_info = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_info.Ids = target_face_ids
    named_selections.Children[9].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[9].Location = sel_info

    ###SUPPORT Assignment
    #Support Assignment 1
    #Select the correct faces
    tolerance = 1e-3
    faces_matchingxy = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_xy_plane = True
                    for vertex in face.Vertices:
                        if abs(vertex.Z) > tolerance:
                            all_on_xy_plane = False
                            break
                    if all_on_xy_plane:
                        faces_matchingxy.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matchingxy

    # Create or assign to a named selection
    face_named = named_selections.Children[2]  # or use AddNamedSelection() to create new
    face_named.ScopingMethod = GeometryDefineByType.Geometry
    face_named.Location = sel_faces
    
    #Support Assignment 2
    #Select the correct faces
    tolerance = 1e-2
    faces_matching_xz_at_y600 = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_xz_y600 = True
                    for vertex in face.Vertices:
                        if abs(vertex.Y - 0.6) > tolerance:
                            all_on_xz_y600 = False
                            break
                    if all_on_xz_y600:
                        faces_matching_xz_at_y600.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matching_xz_at_y600

    # Assign to named_selections.Children[7] (or any slot you'd like)
    named_selections.Children[7].ScopingMethod = GeometryDefineByType.Geometry
    named_selections.Children[7].Location = sel_faces
    
    
    #####SYMMETRY2
    faces_matchingxz = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_xz_plane = True
                    for vertex in face.Vertices:
                        if abs(vertex.Y) > tolerance:
                            all_on_xz_plane = False
                            break
                    if all_on_xz_plane:
                        faces_matchingxz.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matchingxz

    # Create or assign to a named selection
    face_named = named_selections.Children[3]  # or use AddNamedSelection() to create new
    face_named.ScopingMethod = GeometryDefineByType.Geometry
    face_named.Location = sel_faces

    
    #Solution Assignment
    sol=DataModel.AnalysisByName("Static Structural")
    MaxPrinStressGlass=sol.Solution.Children[2]
    MaxPrinStressGlass.Location=Model.NamedSelections.Children[0]
    MaxPrinStressInt=sol.Solution.Children[3]
    MaxPrinStressInt.Location=Model.NamedSelections.Children[1]
    MinPrinStressGlass=sol.Solution.Children[4]
    MinPrinStressGlass.Location=Model.NamedSelections.Children[0]
    MinPrinStressInt=sol.Solution.Children[5]
    MinPrinStressInt.Location=Model.NamedSelections.Children[1]
    ##Contact Assignment
    
    all_contacts = Model.Connections
    contactgroup = all_contacts.Children[0]

    for i,contact in enumerate(contactgroup.Children):
        contact.ContactType = ContactType.Frictional
        contact.FrictionCoefficient = 0.2
        if i > 197:
            contact.ContactType = ContactType.Frictionless


    pass

geometry_object=Model.Geometry
after_geometry_changed(this, geometry_object)