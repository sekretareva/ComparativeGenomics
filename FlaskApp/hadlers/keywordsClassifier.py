import pandas as pd
import re

def keywordsClassify(function, data):
    kwClf = data.getKwCls()
    count = 0

    if function not in kwClf['Function'].unique():
        if 'antibiotic' in function.lower() and 'biosynthesis' in function.lower():
            kwClf = kwClf.append({'Category':'Secondary Metabolism', 
                              'System':'Bacterial cytostatics, differentiation factors and antibiotics', 
                              'Subsystem':'Antibiotics biosynthesis', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'dna polymerase' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA replication', 
                              'Subsystem':'DNA polymerase', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'methylase' in function.lower() and 'rna' not in function.lower() and ('dna' in function.lower() or 'modification' in function.lower()):
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA Metabolism - no subcategory', 
                              'Subsystem':'DNA methylation', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if re.match(r'^T[1-6]SS', function):
            romanNumbers = ['I', 'II', 'III', 'IV', 'V', 'VI']
            type = re.search(r'[1-6]', function).group(0)
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Protein secretion system, Type ' + romanNumbers[int(type)-1], 
                              'Subsystem':'T' + type + ' SS component', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        
        
        if 'integrase' in function.lower():
            kwClf = kwClf.append({'Category':'Phages, Prophages, Transposable elements, Plasmids', 
                              'System':'Transposable elements', 
                              'Subsystem':'Integrase', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        
        if 'transposon' in function.lower():
            kwClf = kwClf.append({'Category':'Phages, Prophages, Transposable elements, Plasmids', 
                              'System':'Transposable elements', 
                              'Subsystem':'Transposon', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'transposase' in function.lower():
            kwClf = kwClf.append({'Category':'Phages, Prophages, Transposable elements, Plasmids', 
                              'System':'Transposable elements', 
                              'Subsystem':'Transposase', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'response regulator' in function.lower() or 'histidine kinase' in function.lower() or ('two-component' in function.lower() and ('response' in function.lower() or 'sensor' in function.lower())):
            kwClf = kwClf.append({'Category':'Regulation and Cell signaling', 
                              'System':'Regulation and Cell signaling - no subcategory', 
                              'Subsystem':'Two-component regulatory system', 
                              'Function':function}, ignore_index=True)
            count+=1
            if 'dna' in function.lower() and ' binding' in function.lower():
                kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'Transcription', 
                              'Subsystem':'Two-component regulatory system', 
                              'Function':function}, ignore_index=True)
        
        if 'nuclease' in function.lower():                
            if 'dna' in function.lower() or 'deoxyribo' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                        'System':'DNA Metabolism - no subcategory', 
                                        'Subsystem':'Nuclease', 
                                        'Function':function}, ignore_index=True)
                count+=1
            if  ('rna' in function.lower() or 'ribo' in function.lower()) and 'deoxyribo' not in function.lower():
                kwClf = kwClf.append({'Category':'RNA Metabolism', 
                                        'System':'RNA processing and modification', 
                                        'Subsystem':'Nuclease', 
                                        'Function':function}, ignore_index=True)
                count+=1
            if 'dna' not in function.lower() and 'rna' not in function.lower() and  'ribo' not in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                        'System':'DNA Metabolism - no subcategory', 
                                        'Subsystem':'Nuclease', 
                                        'Function':function}, ignore_index=True)
                kwClf = kwClf.append({'Category':'RNA Metabolism', 
                                        'System':'RNA processing and modification', 
                                        'Subsystem':'Nuclease', 
                                        'Function':function}, ignore_index=True)
                count+=1
        
        if 'siderophore' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Membrane Transport - no subcategory', 
                              'Subsystem':'Siderophore', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'rod shape' in function.lower():
            kwClf = kwClf.append({'Category':'Cell Wall and Capsule', 
                              'System':'Cell Wall and Capsule - no subcategory', 
                              'Subsystem':'Cell shape', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'protein translocase' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Protein transport', 
                              'Subsystem':'Protein transport', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'dipeptidase' in function.lower():
            kwClf = kwClf.append({'Category':'Protein Metabolism', 
                              'System':'Protein degradation', 
                              'Subsystem':'Dipeptidases', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if ('protease' in function.lower() or 'peptidase' in function.lower()) and 'aminopeptidase' not in function.lower() and 'dipeptidase' not in function.lower() and 'synthase' not in function.lower():
            kwClf = kwClf.append({'Category':'Protein Metabolism', 
                              'System':'Protein degradation', 
                              'Subsystem':'Protein degradation', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'sigma factor' in function.lower():
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'Transcription', 
                              'Subsystem':'Transcription initiation, bacterial sigma factors', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'rna' in function.lower() and ('methyltransferase' in function.lower() or 'mnm' in function.lower() or 'methylase' in function.lower()):
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA processing and modification', 
                              'Subsystem':'RNA methylation', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'rna' in function.lower() and 'methylthiotransferase' in function.lower():
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA processing and modification', 
                              'Subsystem':'tRNA methylthiolation', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if ('polyribonucleotide' in function.lower() or 'rna' in function.lower()) and 'nucleotidyltransferase' in function.lower():
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA processing and modification', 
                              'Subsystem':'RNA processing and degradation, bacterial', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'rna' in function.lower() and 'pseudouridine' in function.lower():
              kwClf = kwClf.append({'Category':'RNA Metabolism', 
                                      'System':'RNA processing and modification', 
                                      'Subsystem':'Pseudouridinylation', 
                                      'Function':function}, ignore_index=True)
              count+=1
        
        if 'aminopeptidase' in function.lower():
            kwClf = kwClf.append({'Category':'Protein Metabolism', 
                              'System':'Protein degradation', 
                              'Subsystem':'Aminopeptidases', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'helicase' in function.lower():
            if 'dna' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA Metabolism - no subcategory', 
                              'Subsystem':'DNA helicase', 
                              'Function':function}, ignore_index=True)
            count+=1
            if 'rna' in function.lower():
                kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA Metabolism - no subcategory', 
                              'Subsystem':'RNA helicase', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'aerotolerance' in function.lower() or 'BatA' in function or 'BatB' in function or 'BatC' in function or 'BatD' in function or 'BatE' in function:
            kwClf = kwClf.append({'Category':'Stress Response', 
                              'System':'Oxidative stress', 
                              'Subsystem':'Aerotolerance', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'vgrg' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Protein secretion system, Type VI', 
                              'Subsystem':'Actin cross-linking toxin', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'cell division' in function.lower() and ('protein' in function.lower() or 'trigger' in function.lower()):
            kwClf = kwClf.append({'Category':'Cell Division and Cell Cycle', 
                              'System':'Cell Division and Cell Cycle - no subcategory', 
                              'Subsystem':'Cell division protein', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'restriction' in function.lower() and ('modification' in function.lower() or 'methylase' in function.lower()):
            if 'type i ' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                  'System':'DNA Metabolism - no subcategory', 
                                  'Subsystem':'Type I Restriction-Modification', 
                                  'Function':function}, ignore_index=True)
                count+=1
            if 'type ii ' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                  'System':'DNA Metabolism - no subcategory', 
                                  'Subsystem':'Type II Restriction-Modification', 
                                  'Function':function}, ignore_index=True)
                count+=1
            if 'type iii ' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                  'System':'DNA Metabolism - no subcategory', 
                                  'Subsystem':'Type III Restriction-Modification', 
                                  'Function':function}, ignore_index=True)
                count+=1
            if 'type iv ' in function.lower():
                kwClf = kwClf.append({'Category':'DNA Metabolism', 
                                  'System':'DNA Metabolism - no subcategory', 
                                  'Subsystem':'Type IV Restriction-Modification', 
                                  'Function':function}, ignore_index=True)
                count+=1
            
        if 'restriction enzyme' in function.lower() or 'restriction endonuclease' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA Metabolism - no subcategory', 
                              'Subsystem':'Restriction Enzyme', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        
        if 'cluster' in function.lower() and 'iron' in function.lower() and 'sulfur' in function.lower():
            kwClf = kwClf.append({'Category':'Miscellaneous', 
                              'System':'Plant-Prokaryote DOE project', 
                              'Subsystem':'Iron-sulfur cluster assembly', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'lipoprotein' in function.lower() and 'releas' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'ABC transporters', 
                              'Subsystem':'Lipoprotein-releasing system', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'lipopolysaccharide' in function.lower() and 'synthesis' in function.lower() and 'export' not in function.lower() and 'capsular' not in function.lower():
            kwClf = kwClf.append({'Category':'Cell Wall and Capsule', 
                              'System':'Gram-Negative cell wall components', 
                              'Subsystem':'Lipopolysaccharides', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'polysaccharide' in function.lower() and 'synthesis' in function.lower() and 'export' not in function.lower() and 'capsular' not in function.lower():
            kwClf = kwClf.append({'Category':'Carbohydrates', 
                              'System':'Polysaccharides', 
                              'Subsystem':'Polysaccharide biosynthesis', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'lpt' in function.lower() and 'protein' in function.lower():
            kwClf = kwClf.append({'Category':'Cell Wall and Capsule', 
                              'System':'Gram-Negative cell wall components', 
                              'Subsystem':'Lipoprotein sorting system', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'capsular' in function.lower() and 'polysaccharide' in function.lower() and 'synthesis' in function.lower():
            kwClf = kwClf.append({'Category':'Cell Wall and Capsule', 
                              'System':'Capsular and extracellular polysacchrides', 
                              'Subsystem':'Capsular Polysaccharides Biosynthesis and Assembly', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'crisp' in function.lower() and 'repeat' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'CRISPs', 
                              'Subsystem':'CRISPRs', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'crisp' in function.lower() and 'spacer' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'CRISPs', 
                              'Subsystem':'Spacers', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'crisp' in function.lower() and ('ramp' in function.lower() or 'cas' in function.lower()):
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'CRISPs', 
                              'Subsystem':'CRISPR-associated proteins', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'transport' in function.lower() and 'ABC' not in function and ('antiport' not in function.lower() or 'symport' not in function.lower() or 'uniport' not in function.lower()):
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Membrane Transport - no subcategory', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'ABC' not in function and 'antiport' in function.lower() or 'symport' in function.lower() or 'uniport' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Uni- Sym- and Antiporters', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'resist' in function.lower() and 'phage' not in function.lower():
            kwClf = kwClf.append({'Category':'Virulence, Disease and Defense', 
                              'System':'Resistance to antibiotics and toxic compounds', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'resist' in function.lower() and 'phage' in function.lower():
            kwClf = kwClf.append({'Category':'Virulence, Disease and Defense', 
                              'System':'Virulence, Disease and Defense - no subcategory', 
                              'Subsystem':'Phage defence', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'cytochrome' in function.lower():
            kwClf = kwClf.append({'Category':'Respiration', 
                              'System':'Respiration - no subcategory', 
                              'Subsystem':'Cytochrome', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'heat' in function.lower() and 'shock' in function.lower():
            kwClf = kwClf.append({'Category':'Stress Response', 
                              'System':'Heat shock', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'cold' in function.lower() and 'shock' in function.lower():
            kwClf = kwClf.append({'Category':'Stress Response', 
                              'System':'Cold shock', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'cold' in function.lower() and 'shock' in function.lower():
            kwClf = kwClf.append({'Category':'Stress Response', 
                              'System':'Stress Response - no subcategory', 
                              'Subsystem':'Phage shock', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'ABC' in function and 'transport' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'ABC-transporters', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'tonB' in function or 'TonB' in function:
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Membrane Transport - no subcategory', 
                              'Subsystem':'Ton and Tol transopt system', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'ribosomal protein' in function.lower():
            kwClf = kwClf.append({'Category':'Protein Metabolism', 
                              'System':'Protein biosynthesis', 
                              'Subsystem':'Ribosome LSU/SSU bacterial', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'dna' in function.lower() and 'repair' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA repair', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'tRNA-' in function and len(function)<16:
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA processing and modification', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'transcription' in function.lower() and 'regulator' in function.lower():
            kwClf = kwClf.append({'Category':'RNA Metabolism', 
                              'System':'RNA processing and modification', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'type' in function.lower() and 'secretion' in function.lower():
            kwClf = kwClf.append({'Category':'Membrane Transport', 
                              'System':'Protein secretion system', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1
        
        if 'topoisomerase' in function.lower():
              kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA replication', 
                              'Subsystem':'DNA topoisomerases', 
                              'Function':function}, ignore_index=True)
              count+=1
        
        if 'replication' in function.lower():
            kwClf = kwClf.append({'Category':'DNA Metabolism', 
                              'System':'DNA replication', 
                              'Subsystem':'none', 
                              'Function':function}, ignore_index=True)
            count+=1

    data.setKwCls(kwClf)